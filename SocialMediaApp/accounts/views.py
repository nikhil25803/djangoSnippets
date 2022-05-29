from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from urllib3 import HTTPResponse
# Create your views here.


def homepage(request):

    return render(request, 'home.html')


def signup_view(request):

    if request.method == 'POST':
        name = request.POST.get('fullname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')
        if password == confirm_password:
            user = User.objects.create(username=username,
                                       email=email, password=password, first_name=name)
            messages.success(request, "User Created")

            return render(request, 'login.html')

        # print( username, email, password, confirm_password)

    return render(request, 'signup.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'home.html')
        else:
            return HttpResponse("Invalid Credentials")

    return render(request, 'login.html')
