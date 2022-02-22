import email
import imp
from unicodedata import name
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from .forms import register
from .models import User
# Create your views here.

def home(request):
    if request.method == 'POST':
        fm = register(request.POST)
        if fm.is_valid():
            fn = fm.cleaned_data['first_name']
            ln = fm.cleaned_data['last_name']
            em = fm.cleaned_data['email']
            tn = fm.cleaned_data['twitter_name']
            us = fm.cleaned_data['username']
            # reg = User(fir=fn, email=em)
            fm.save()
            fm = register()
            stud = User.objects.all()
            
            
    
    else:
        fm = register()
        
        
        

    return render(request, 'card/home.html', {'form':fm, 'stud':stud})

def delete(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def cards(request):
    return render(request, 'card/cards.html')

def profiles(request):
    return render(request, 'card/profiles.html')

