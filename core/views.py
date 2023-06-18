from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):

#  check if user is logged in or not
    return render(request, 'index.html')

def product(request):

    #  check if user is logged in or not
    return render(request, 'product.html')

def product_register(request):

    return render(request, 'product_register.html')



def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username= username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login_page')

        else:
            user = authenticate(username = username , password = password)

            if user is None:
                messages.error(request, 'Invalid Password')
                return redirect('/login_page/')

            else:
                login(request, user)
                return redirect('index')
    else:
        return render(request, 'login_page.html')


def signup(request):

    if request.method == "POST":

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            return redirect('/signup')

        else:
            user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )
            user.set_password(password)
            user.save()

            return redirect('index')
            

    return render(request, 'signup.html')


def logout_page(request):
    logout(request)
    return redirect('/login_page/')


