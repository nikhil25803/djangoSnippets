from django.shortcuts import render

# Create your views here.
from .forms import ProjectForm
from .models import Project
from django.views import View
# from django.views.decorators.csrf import csrf_protect

# @csrf_protect
class HomeView(View):
    def get(self, request):
        form = ProjectForm()
        #users = ProjectForm.objects.all()
        return render(request, 'prapp/home.html',{'form':form})

    def post(self, request):
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            form = ProjectForm()
            return render(request, 'prapp/home.html',{'form':form})
