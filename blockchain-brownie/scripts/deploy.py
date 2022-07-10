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


def createsolution(name, problem, index):
    suggestion = problem_dict[problem]  # grabbing the latest suggestion
    flag = suggestion.newsolution(name, "Buy more stuff", 12, {
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
    print(a(accounts[2]))


def endpoll(problem):
    suggestion = problem_dict[problem]
    contract = suggestion.endsuggestion({
        "from": accounts[0]
    })
    print(contract.return_value)


def main():
    run('a')
    createsolution('bender', "a", 1)
    vote('a')
    createsolution('leeela', "a", 0)
    vote('a')
    createsolution('fry', "a", 2)
    vote('a')
    endpoll('a')
