from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, 'index.html')

def product(request):
    return render(request, 'product.html')


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username= username).exists():
            return redirect('/login_page')

        else:
            user = authenticate(username = username , password = password)

            if user is None:
                return redirect('/login_page')

            else:
                login(request, user)
                return render('/index')

    else:
        return render(request, 'login_page.html')


def signup(request):

    return render(request, 'signup.html')

