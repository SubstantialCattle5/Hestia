import json

import web3.eth
from solcx import compile_standard, install_solc
from web3 import Web3
from web3.auto import w3


class Deploy_Suggestion:
    def __init__(self, private_key, address, problem):
        with open("./Suggestion.sol", "r") as file:
            self.suggestion_file = file.read()
        self.address = address
        self.pvt_key = private_key
        self.problem = problem

    def deploy(self):
        # compile our solidity
        install_solc("0.8.0")
        compile_sol = compile_standard(
            {
                "language": "Solidity",
                "sources": {
                    "Suggestion.sol": {
                        "content": self.suggestion_file
                    }
                },
                "settings": {
                    "outputSelection": {
                        "*": {
                            "*": ['abi', 'metadata', 'evm.bytecode', 'evm.sourceMap']
                        }
                    }
                },

            },
            solc_version="0.8.0",
        )

        with open("compiled_code.json", "w") as file:
            json.dump(compile_sol, file, indent=2)

        # get bytecode
        bytecode = compile_sol["contracts"]["Suggestion.sol"]["Suggestion"]["evm"]["bytecode"]["object"]
        # get abi
        abi = compile_sol["contracts"]["Suggestion.sol"]["Suggestion"]["abi"]

        # for connecting to ganache
        w3 = Web3(Web3.HTTPProvider("http://0.0.0.0:8545"))
        chain_id = 1337

        # Creating the contract
        Suggestion = w3.eth.contract(abi=abi, bytecode=bytecode)

        # Getting the latest transaction
        nonce = w3.eth.getTransactionCount(self.address)

        # Submit the transaction that deploys the contract

        transaction = Suggestion.constructor(self.problem).buildTransaction(
            {
                "chainId": chain_id,
                "gasPrice": w3.eth.gas_price,
                "from": self.address,
                "nonce": nonce,
            }
        )
        # Sign
        signed_txn = w3.eth.account.sign_transaction(transaction, private_key=self.pvt_key)
        print("Deploying the contract!")
        # send it
        tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        # wait
        tx_reciept = w3.eth.wait_for_transaction_receipt(tx_hash)
        print(f'Contract deployed {tx_reciept.contractAddress}')

        return tx_reciept.contractAddress


def main():
    obj = Deploy_Suggestion(private_key="0xeed015846a770c92010156f31171e52b39202cef0ae9d5edbea8792671d2d416",
                            address="0x5742bcFD2b4006aF9e431A3BEE7d9116c30f988a",
                            problem="Eat icecream")
    address = obj.deploy()


if __name__ == "__main__":
    main()
