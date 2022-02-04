from django.shortcuts import render

# Create your views here.
from .forms import ProjectForm
from .models import Project
from django.views import View

class HomeView(View):
    def get(self, request):
        form = ProjectForm()
        return render(request, 'prapp/home.html', {'form':form})
