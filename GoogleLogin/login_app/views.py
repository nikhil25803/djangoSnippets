from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'index.html')


def login(request):

    return render(request, 'login_page.html')


def register(request):

    return render(request, 'register_page.html')