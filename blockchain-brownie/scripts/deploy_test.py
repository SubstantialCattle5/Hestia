from brownie import Voting2, accounts


def deploy():
    voters_list = [accounts[1], accounts[2], accounts[3]]
    voting = Voting2.deploy(accounts[1], voters_list, {
        'from': accounts[0],

    })


def vote():
    contract = Voting2[-1]
    contract.voting(True, {
        "from": accounts[1],
    })
    print(f"Vote Status: {contract.vote()} ")
    contract.voting(True, {
        "from": accounts[3]
    })
    print(f"Vote Status: {contract.vote()} ")
    contract.voting(False, {
        "from": accounts[2]
    })
    print(f"Vote Status: {contract.vote()} ")
    contract.fund({
        "from": accounts[2],
        "value": 20000000000
    })
    print(f"Balance of the contract {contract.balance()}" )
    contract.withdraw({
        "from": accounts[0]
    })
    print(f'Contract goes to {contract.vote()}')
    print(f"Contract Balance : {contract.balance()} ")
    print(f"Accounts Balance : {accounts[1].balance()} ")


def main():
    deploy()
    vote()
