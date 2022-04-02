# import imp
from django.shortcuts import redirect, render
# from matplotlib.pyplot import title
from . models import Todo
# Create your views here.


def index(request):

    todo = Todo.objects.all()

    if request.method == 'POST':
        new_todo = Todo(
            title = request.POST['title']
        )
        new_todo.save()
        return redirect('/')

    return render(request, 'index.html', {'todos':todo})