import json

from django.shortcuts import render

# Create your views here.
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from core.models import Questions
from blockchain_deployment import deploy_suggestion as ds

# Create your views here.

contracts = dict()


def index(request):
    if request.method == "POST":
        if 'login' in request.POST:
            return redirect("login")
        # CHANGE
        elif 'signup' in request.POST:
            return redirect("signup")
        elif 'menu' in request.POST:
            return redirect("main_pg")
    return render(request, "index.html")


def login(request):
    if request.method == 'POST':
        username, password = request.POST['username'], request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Password is Wrong!")
            return redirect('login')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


# ------------------ Signup----------------------
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User already exist')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,
                                                password=password)
                user.save()

                # log user in and redirect to settings page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                return redirect('index')

        else:
            messages.info(request, 'Password not Matching')
            return redirect('signup')
    else:
        return render(request, 'signup.html')


questions = list()


def main_pg(request):
    if request.method == "POST":
        global contracts
        if 'save' in request.POST:
            task = request.POST['task']
            address = request.POST['address']
            pvt_key = request.POST['pvt_key']
            new_contract = ds.Deploy_Suggestion(address=address, private_key=pvt_key)
            address = new_contract.deploy(problem=task)
            contracts[new_contract] = [address, task]
            questions.append(task)
        return redirect('problems')
    return render(request, 'main_pg.html')


index2 = int()


def problems(request):
    global questions
    for index in contracts:
        questions.append(contracts[index][1])
    if request.method == 'POST':
        global index2
        index2 = request.POST["index"]
        return redirect("solution")
    return render(request, "problems.html", {
        "questions": questions
    })


def solution(request):
    print(questions)
    print(index2)
    question = questions[int(index2) - 1]
    if request.method == "POST" :
        address = request.POST["address"]
        name = request.POST["name"]
        answer = request.POST["answer"]
        cost = request.POST["cost"]

    return render(request, "solution.html", {
        "question": question
    })
