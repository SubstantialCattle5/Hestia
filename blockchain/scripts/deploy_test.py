from brownie import Voting, accounts


def deploy():
    voting = Voting.deploy("0xD03036BEd8208d3f96c00edF0b5Ada3D3DE47152", 20, {
        'from': accounts[0]
    })


def vote():
    contract = Voting[-1]
    contract.vote(False, {
        "from": accounts[1]
    })
    print(contract.paying_check())
    contract.vote(True, {
        "from": accounts[1]
    })
    print(contract.paying_check())
    contract.vote(True, {
        "from": accounts[2]
    })
    print(contract.paying_check())


def main():
    deploy()
    vote()
