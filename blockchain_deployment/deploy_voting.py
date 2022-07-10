import json

from solcx import install_solc, compile_standard
from web3 import Web3


class Deploy_Voting:
    def __init__(self, private_key, address):
        """
        @note : initializes the abi . w3
        :param private_key: string
        :param address: string - user user_address
        """
        with open("./Voting.sol", "r") as file:
            self.voting_file = file.read()
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

    def deploy(self, winner: str, funds: int, check: list):
        """
        @note : deploys the contract suggestion
        :param check:
        :param funds:
        :param winner:
        :return: user_address of the deployed contract

        """
        # compile our solidity
        install_solc("0.8.0")
        compile_sol = compile_standard(
            {
                "language": "Solidity",
                "sources": {
                    "Voting.sol": {
                        "content": self.voting_file
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

        with open("compiled_code2.json", "w") as file:
            json.dump(compile_sol, file, indent=2)

        # get bytecode
        self.bytecode = compile_sol["contracts"]["Voting.sol"]["Voting"]["evm"]["bytecode"]["object"]
        # get abi
        self.abi = compile_sol["contracts"]["Voting.sol"]["Voting"]["abi"]

        # Creating the contract
        Voting = self.w3.eth.contract(abi=self.abi, bytecode=self.bytecode)

        # Submit the transaction that deploys the contract
        print(check)
        transaction = Voting.constructor(winner, funds, check).buildTransaction(
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

    def vote(self, address):
        return


def main():
    supervisors = ["0x0481AE65E5088a35727B2294071aA1Bc62804A2b", "0x28B469B6668B42671e29374dDf10c88Fa35cf777"]
    obj = Deploy_Voting(address="0xD03036BEd8208d3f96c00edF0b5Ada3D3DE47152",
                        private_key="0x6b8316255c09630c67abbb411da34ecd8fb91ef87dd5c7afd19de234cc0c7237")

    address = obj.deploy(winner="0x0481AE65E5088a35727B2294071aA1Bc62804A2b", funds=5, check=supervisors)
    print(address)


if __name__ == "__main__":
    main()
