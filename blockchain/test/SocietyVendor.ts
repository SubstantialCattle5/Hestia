import { expect } from "chai";
import { ethers } from "hardhat";
import { SocietyVendor } from "../typechain/SocietyVendor";
import { SignerWithAddress } from "@nomiclabs/hardhat-ethers/signers";

describe("SocietyVendor", () => {
  let societyVendor: SocietyVendor;
  let society: SignerWithAddress;
  let vendor: SignerWithAddress;

  beforeEach(async () => {
    const signers = await ethers.getSigners();
    society = signers[0];
    vendor = signers[1];

    const SocietyVendorFactory = await ethers.getContractFactory(
      "SocietyVendor",
      society
    );
    societyVendor = (await SocietyVendorFactory.deploy()) as SocietyVendor;
    await societyVendor.deployed();
  });

  it("should allow societies to register", async () => {
    await societyVendor.connect(society).registerSociety();
    expect(await societyVendor.isSociety(society.address)).to.be.true;
  });

  it("should allow vendors to register", async () => {
    await societyVendor.connect(vendor).registerVendor();
    expect(await societyVendor.isVendor(vendor.address)).to.be.true;
  });

  it("should allow societies to create requests", async () => {
    await societyVendor.connect(society).registerSociety();
    await societyVendor
      .connect(society)
      .createRequest("Test request", Date.now() + 1000 * 60 * 60 * 24, 100);
    const request = await societyVendor.getRequest(0);
    expect(request.description).to.equal("Test request");
    expect(request.budget).to.equal(100);
  });

  it("should allow vendors to create tenders for requests", async () => {
    await societyVendor.connect(society).registerSociety();
    await societyVendor
      .connect(society)
      .createRequest("Test request", Date.now() + 1000 * 60 * 60 * 24, 100);
    await societyVendor.connect(vendor).registerVendor();
    await societyVendor
      .connect(vendor)
      .createTender(0, 90, "Test tender description");
    const tender = await societyVendor.getTender(0);
    expect(tender.description).to.equal("Test tender description");
    expect(tender.amount).to.equal(90);
  });

  it("should allow societies to cast votes for tenders", async () => {
    await societyVendor.connect(society).registerSociety();
    await societyVendor
      .connect(society)
      .createRequest("Test request", Date.now() + 1000 * 60 * 60 * 24, 100);
    await societyVendor.connect(vendor).registerVendor();
    await societyVendor
      .connect(vendor)
      .createTender(0, 90, "Test tender description");
    await societyVendor.connect(society).castVote(0);
    expect(await societyVendor.getNumberOfVotes(0)).to.equal(1);
  });

  it("should allow societies to select a winning tender", async () => {
    await societyVendor.connect(society).registerSociety();
    await societyVendor
      .connect(society)
      .createRequest("Test request", Date.now() + 1000 * 60 * 60 * 24, 100);
    await societyVendor.connect(vendor).registerVendor();
    await societyVendor
      .connect(vendor)
      .createTender(0, 90, "Test tender description");
    await societyVendor.connect(society).castVote(0);
    const [winningTender] = await societyVendor.selectWinner(0, 1);
    expect(winningTender.id).to.equal(0);
  });

  it("should allow societies to deploy a contract with the winning vendor", async () => {
    await societyVendor.connect(society).registerSociety();
    await societyVendor
      .connect(society)
      .createRequest("Test request", Date.now() + 1000 * 60 * 60 * 24, 100);
    await societyVendor.connect(vendor).registerVendor();
    await societyVendor
      .connect(vendor)
      .createTender(0, 90, "Test tender description");
    await societyVendor.connect(society).castVote(0);
    const [winningTender] = await societyVendor.selectWinner(0, 1);
    const timeLimit = Date.now() + 1000 * 60 * 60 * 24;
    const amount = winningTender.amount;
    await societyVendor
      .connect(society)
      .deployContract(0, winningTender.id, timeLimit, amount, {
        value: amount,
      });
  });
  it("should allow societies to edit requests", async () => {
    await societyVendor.connect(society).registerSociety();
    await societyVendor
      .connect(society)
      .createRequest("Test request", Date.now() + 1000 * 60 * 60 * 24, 100);
    await societyVendor
      .connect(society)
      .editRequest(0, "Updated request", Date.now() + 1000 * 60 * 60 * 48, 200);
    const request = await societyVendor.getRequest(0);
    expect(request.description).to.equal("Updated request");
    expect(request.budget).to.equal(200);
  });

  it("should allow societies to view contract details", async () => {
    await societyVendor.connect(society).registerSociety();
    await societyVendor
      .connect(society)
      .createRequest("Test request", Date.now() + 1000 * 60 * 60 * 24, 100);
    await societyVendor.connect(vendor).registerVendor();
    await societyVendor
      .connect(vendor)
      .createTender(0, 90, "Test tender description");
    await societyVendor.connect(society).castVote(0);
    const [winningTender] = await societyVendor.selectWinner(0, 1);
    const timeLimit = Date.now() + 1000 * 60 * 60 * 24;
    const amount = winningTender.amount;
    await societyVendor
      .connect(society)
      .deployContract(0, winningTender.id, timeLimit, amount, {
        value: amount,
      });
    const contractDetails = await societyVendor.getContractDetails(0);
    expect(contractDetails.amount).to.equal(amount);
  });
  it("should not allow non-societies to create requests", async () => {
    await expect(
      societyVendor
        .connect(vendor)
        .createRequest("Test request", Date.now() + 1000 * 60 * 60 * 24, 100)
    ).to.be.revertedWith("Only societies can call this function");
  });

  it("should not allow non-vendors to create tenders", async () => {
    await expect(
      societyVendor
        .connect(society)
        .createTender(0, 90, "Test tender description")
    ).to.be.revertedWith("Only vendors can call this function");
  });

  it("should not allow non-societies to cast votes", async () => {
    await societyVendor
      .connect(society)
      .createRequest("Test request", Date.now() + 1000 * 60 * 60 * 24, 100);
    await societyVendor.connect(vendor).registerVendor();
    await societyVendor
      .connect(vendor)
      .createTender(0, 90, "Test tender description");
    await expect(societyVendor.connect(vendor).castVote(0)).to.be.revertedWith(
      "Only societies can call this function"
    );
  });

  it("should not allow non-societies to select a winner", async () => {
    await societyVendor.connect(society).registerSociety();
    await societyVendor
      .connect(society)
      .createRequest("Test request", Date.now() + 1000 * 60 * 60 * 24, 100);
    await societyVendor.connect(vendor).registerVendor();
    await societyVendor
      .connect(vendor)
      .createTender(0, 90, "Test tender description");
    await expect(
      societyVendor.connect(vendor).selectWinner(0, 1)
    ).to.be.revertedWith("Only societies can call this function");
  });

  it("should not allow non-societies to deploy a contract", async () => {
    await societyVendor.connect(society).registerSociety();
    await societyVendor
      .connect(society)
      .createRequest("Test request", Date.now() + 1000 * 60 * 60 * 24, 100);
    await societyVendor.connect(vendor).registerVendor();
    await societyVendor
      .connect(vendor)
      .createTender(0, 90, "Test tender description");
    const timeLimit = Date.now() + 1000 * 60 * 60 * 24;
    const amount = ethers.utils.parseEther("1");
    await expect(
      societyVendor
        .connect(vendor)
        .deployContract(0, 0, timeLimit, amount, { value: amount })
    ).to.be.revertedWith("Only societies can call this function");
  });
});
