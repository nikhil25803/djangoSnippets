
import re
from django.shortcuts import render
from django.views.generic import TemplateView
from  django.contrib.auth.decorators import login_required

def index(request):

    return render(request, 'home.html')

@login_required
def login_page(request):

    return render(request, 'login.html')