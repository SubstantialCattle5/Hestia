import { HardhatUserConfig } from "hardhat/config";
import "@nomicfoundation/hardhat-toolbox";
import "solidity-docgen";

const config: HardhatUserConfig = {
  solidity: "0.8.18",
  paths: {
    sources: "./contracts",
  },
};

export default config;
