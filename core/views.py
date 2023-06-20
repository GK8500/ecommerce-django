from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *

@login_required(login_url="/login_page/")
# Create your views here.

def index(request):
    queryset = Product.objects.all()
    context = {'product' : queryset}

    return render(request, 'index.html', context)


#  check if user is logged in or not
    # return render(request, 'index.html')

def product(request):

    #  check if user is logged in or not
    return render(request, 'product.html')

def product_register(request):
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        price = data.get('price')
        desc = data.get('desc')
        image = request.FILES.get('image')

        Product.objects.create(
            name = name,
            price = price,
            desc = desc,
            image = image,
        )
        queryset = Product.objects.all()
        context = {'product' : queryset}
        return redirect('index')

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


