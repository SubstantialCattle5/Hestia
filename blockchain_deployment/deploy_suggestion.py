import json

import web3.eth
from solcx import compile_standard, install_solc
from web3 import Web3


class Deploy_Suggestion:
    def __init__(self, private_key, address):
        """
        @note : initializes the abi . w3
        :param private_key: string
        :param address: string - user user_address
        """
        with open("./Suggestion.sol", "r") as file:
            self.suggestion_file = file.read()
        self.user_address = address
        self.pvt_key = private_key
        # for connecting to ganache
        self.w3 = Web3(Web3.HTTPProvider("http://0.0.0.0:8545"))
        self.chain_id = 1337

        # Getting the latest transaction
        self.nonce = self.w3.eth.getTransactionCount(self.user_address)
        self.count = 0

        # To check if the user has voted or not
        self.flag = False

    def deploy(self, problem):
        """
        @note : deploys the contract suggestion
        :param problem:
        :return: user_address of the deployed contract

        """
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
        self.bytecode = compile_sol["contracts"]["Suggestion.sol"]["Suggestion"]["evm"]["bytecode"]["object"]
        # get abi
        self.abi = compile_sol["contracts"]["Suggestion.sol"]["Suggestion"]["abi"]

        # Creating the contract
        Suggestion = self.w3.eth.contract(abi=self.abi, bytecode=self.bytecode)

        # Submit the transaction that deploys the contract

        transaction = Suggestion.constructor(problem).buildTransaction(
            {
                "chainId": self.chain_id,
                "gasPrice": self.w3.eth.gas_price,
                "from": self.user_address,
                "nonce": self.nonce,
            }
        )
        # Sign
        signed_txn = self.w3.eth.account.sign_transaction(transaction, private_key=self.pvt_key)
        print("Deploying the contract!")
        # send it
        tx_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        # wait
        tx_reciept = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        print(f'Contract deployed {tx_reciept.contractAddress}')

        return tx_reciept.contractAddress

    def solution(self, contract_address, name, solution, cost):
        self.count += 1
        # Calling the transaction
        Suggestion = self.w3.eth.contract(address=contract_address, abi=self.abi)

        suggestion_given = Suggestion.functions.newsolution(name, solution, cost).buildTransaction(
            {
                "chainId": self.chain_id,
                "gasPrice": self.w3.eth.gas_price,
                "from": self.user_address,
                "nonce": self.nonce + self.count,

            }
        )
        signed_txn = self.w3.eth.account.sign_transaction(
            suggestion_given, private_key=self.pvt_key
        )
        tx_hash = self.w3.eth.send_raw_transaction(
            signed_txn.rawTransaction
        )
        tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)

        return Suggestion.functions.task(self.user_address).call()

    def user_vote(self, vote: bool, contract_address: str, vote_address: str):
        """

        @note - each address  can vote only once.
        :param vote: bool - true : +1 or false : -1
        :param contract_address: address of the deployed contract
        :param vote_address:
        :return: The contract address of the voted suggestion
                 None if already voted

        """
        if not self.flag:
            self.count += 1
            Suggestion = self.w3.eth.contract(address=contract_address, abi=self.abi)
            user_vote_tx = Suggestion.functions.uservote(True, vote_address).buildTransaction(
                {
                    "chainId": self.chain_id,
                    "gasPrice": self.w3.eth.gas_price,
                    "from": self.address ,
                    "nonce": self.nonce + self.count,

                }
            )

            signed_txn = self.w3.eth.account.sign_transaction(
                user_vote_tx, private_key=self.pvt_key
            )
            tx_hash = self.w3.eth.send_raw_transaction(
                signed_txn.rawTransaction
            )
            tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
            self.flag = True
            return Suggestion.functions.task(self.user_address).call()

    def endsuggestion(self, contract_address: str):
        """
        @note - can only be used by the owner of the contract
                ends the poll.
        :param contract_address:
        :return: the winner of the suggestion poll
        """
        self.count += 1
        Suggestion = self.w3.eth.contract(address=contract_address, abi=self.abi)

        suggestion_endpoll = Suggestion.functions.endsuggestion().buildTransaction(
            {
                "chainId": self.chain_id,
                "gasPrice": self.w3.eth.gas_price,
                "from": self.user_address,
                "nonce": self.nonce + self.count,

            }
        )
        signed_txn = self.w3.eth.account.sign_transaction(
            suggestion_endpoll, private_key=self.pvt_key
        )
        tx_hash = self.w3.eth.send_raw_transaction(
            signed_txn.rawTransaction
        )
        tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)

        return Suggestion.functions.winner2().call()


