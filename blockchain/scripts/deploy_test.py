from brownie import Voting2 , accounts


def deploy():
    voters_list = [accounts[1] , accounts[2] , accounts[3]]
    voting = Voting2.deploy(accounts[1], voters_list, {
        'from': accounts[0]
    })


def vote():
    contract = Voting2[-1]
    contract.voting(True , {
        "from": accounts[1]
    })
    print(contract.vote())
    contract.voting(False , {
        "from": accounts[3]
    })
    print(contract.vote())
    contract.voting(True , {
        "from": accounts[2]
    })
    print(contract.vote())

    print(f'Contract goes to {contract.vote()}')

def main():
    deploy()
    vote()
