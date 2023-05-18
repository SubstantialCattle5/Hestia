import { expect } from "chai";
import { ethers } from "hardhat";
import { SocietyVendor } from "../typechain-types";

describe("SocietyVendor", function () {
  let SocietyVendor,
    societyVendor: SocietyVendor,
    owner,
    society: { address: string },
    vendor: { address: string };

  beforeEach(async function () {
    SocietyVendor = await ethers.getContractFactory("SocietyVendor");
    [owner, society, vendor] = await ethers.getSigners();
    societyVendor = await SocietyVendor.deploy();
    await societyVendor.deployed();
  });

  it("should allow societies to register", async function () {
    await societyVendor.connect(society).registerSociety();
    expect(await societyVendor.isSociety(society.address)).to.equal(true);
  });

  it("should allow vendors to register", async function () {
    await societyVendor.connect(vendor).registerVendor();
    expect(await societyVendor.isVendor(vendor.address)).to.equal(true);
  });

  it("should allow societies to create requests", async function () {
    await societyVendor.connect(society).registerSociety();
    await societyVendor
      .connect(society)
      .createRequest("Test request", 12345, 1000);
    const request = await societyVendor.getRequest(0);
    expect(request.description).to.equal("Test request");
    expect(request.deadline).to.equal(12345);
    expect(request.budget).to.equal(1000);
  });

  it("should allow vendors to create tenders", async function () {
    await societyVendor.connect(society).registerSociety();
    await societyVendor
      .connect(society)
      .createRequest("Test request", 12345, 1000);
    await societyVendor.connect(vendor).registerVendor();
    await societyVendor.connect(vendor).createTender(0, 900, "Test tender");
    const tender = await societyVendor.getTender(0);
    expect(tender.requestId).to.equal(0);
    expect(tender.amount).to.equal(900);
    expect(tender.description).to.equal("Test tender");
  });
  it("should allow fetching all tenders for a specific request", async function () {
    await societyVendor.connect(society).registerSociety();
    await societyVendor
      .connect(society)
      .createRequest("Test request", 12345, 1000);
    await societyVendor.connect(vendor).registerVendor();
    await societyVendor.connect(vendor).createTender(0, 900, "Test tender 1");
    await societyVendor.connect(vendor).createTender(0, 800, "Test tender 2");
    const tenders = await societyVendor.getTendersForRequest(0);
    expect(tenders.length).to.equal(2);
    expect(tenders[0].amount).to.equal(900);
    expect(tenders[0].description).to.equal("Test tender 1");
    expect(tenders[1].amount).to.equal(800);
    expect(tenders[1].description).to.equal("Test tender 2");
  });

});
