import imp
from django.shortcuts import render

# Create your views here.

from .forms import ResumeForm
from .models import Resume
from django.views import View


class HomeView(View):
    def get(self, request):
        form  = ResumeForm()
        return render(request, "myapp/home.html", {'form':form})