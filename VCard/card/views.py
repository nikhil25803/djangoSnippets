from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'card/home.html')

def cards(request):
    return render(request, 'card/cards.html')

def profiles(request):
    return render(request, 'card/profiles.html')

