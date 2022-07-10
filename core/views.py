from django.shortcuts import render

# Create your views here.
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    if request.method == "POST":
        if 'login' in request.POST:
            return redirect("login")
        # CHANGE
        elif 'signup' in request.POST:
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


@login_required(login_url='/login')
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


def main_pg(request):
    if request.method == "POST":
        if 'save' in request.POST:
            title = request.POST['title']
            task = request.POST['task']


    return render(request, 'main_pg.html')
