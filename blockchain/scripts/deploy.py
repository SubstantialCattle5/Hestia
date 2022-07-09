from brownie import Suggestion, accounts
from scripts.common import get_account

problem_dict = dict()


def run(_problem: str):
    account = get_account(index=0)
    problem = _problem
    suggestion = Suggestion.deploy(
        problem,
        {"from": account}
    )
    suggestion = Suggestion[-1]
    problem_dict[problem] = suggestion


def createsolution(problem, index):
    suggestion = problem_dict[problem]  # grabbing the latest suggestion
    flag = suggestion.newsolution("nilay", "sleep", 12, {
        'from': accounts[index]
    })
    print(flag)
    a = suggestion.task
    print(a(accounts[index]))


def vote(problem):
    suggestion = problem_dict[problem]
    flag = suggestion.uservote(True, accounts[0], {
        "from": accounts[2]
    })
    a = suggestion.task
    print(a(accounts[0]))
    print(a(accounts[1]))


def endpoll(problem):
    suggestion = problem_dict[problem]
    contract = suggestion.endsuggestion({
        "from": accounts[0]
    })
    print(contract.return_value)


def main():
    run('a')
    createsolution('a', 1)
    vote('a')
    createsolution('a', 0)
    vote('a')
    createsolution('a', 0)
    vote('a')
    endpoll('a')
