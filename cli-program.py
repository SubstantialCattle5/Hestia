from blockchain_deployment import deploy_suggestion as ds
from blockchain_deployment import deploy_voting as dv
from brownie import accounts

##--------------------------CONTRACT OPENING------------------------##

print("Hestia!!!!!!!!!!!")
address = input("Enter your address : ")
private_key = input("Enter your Pvt Key : ")
private_key = "0x" + private_key
# Creating  the object
Contract = ds.Deploy_Suggestion(private_key=private_key, address=address)


def change_acc():
    global address, private_key, Contract
    address = input("Enter your address : ")
    private_key = input("Enter your Pvt Key : ")
    private_key = "0x" + private_key
    # Creating  the object
    Contract = ds.Deploy_Suggestion(private_key=private_key, address=address)


def deploy_contract():
    # Deploying the contract
    problem = input("Enter your Tender :")
    contract_address = Contract.deploy(problem=problem)


def adding_solution():
    # adding solution
    name = input("Name : ")
    if name is None:
        return None
    solution = input("Enter the solution : ")
    cost = int(input("Enter the cost : "))
    contract_address = input("Enter the Contract Address : ")
    call = Contract.solution(contract_address=contract_address, name=name, solution=solution, cost=cost)
    print(call)


def uservote():
    vote = input("Enter your vote : ")
    contract_address = input("Enter the Contract Address : ")
    vote_address = input("Input the Vote Address ")
    a = Contract.user_vote(vote=vote, contract_address=contract_address, vote_address=vote_address)
    print(a)


def endsuggestion():
    print("WARING : only the owner can end tender poll ")
    contract_address = input("Enter the contract address : ")
    winner = Contract.endsuggestion(contract_address=contract_address)
    print(f"WINNER {winner}!!!!!!")


while True:
    print("""Welcome to Hestia!!!!!!!\n
    1) change acc \n
    2) deploy contract \n 
    3) adding solution \n   
    4) Vote on a solution \n 
    5) End the Suggestion Poll \n
    """)
    choice = int(input("Enter you choice :"))
    if choice == 1: change_acc()
    if choice == 2: deploy_contract()
    if choice == 3: adding_solution()
    if choice == 4: uservote()
    if choice == 6: break;
    if choice == 5: endsuggestion()
