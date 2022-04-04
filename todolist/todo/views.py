# import imp
# from distutils.command.config import config
# from django.db import DatabaseError
from django.shortcuts import redirect, render
# from matplotlib.pyplot import title
from . models import Todo
# Create your views here.
import pyrebase

config = {

    "apiKey": "AIzaSyBZveQv0lm1zEOl8FX_rKg76VZWcQ3Z53k",
    "authDomain": "test-a35c8.firebaseapp.com",
    "databaseURL": "https://test-a35c8-default-rtdb.firebaseio.com",
    "projectId": "test-a35c8",
    "storageBucket": "test-a35c8.appspot.com",
    "messagingSenderId": "143099634713",
    "appId": "1:143099634713:web:6f86943dfd640cb10c7688",
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


def index(request):

    todo = Todo.objects.all()

    if request.method == 'POST':
        new_todo = Todo(
            title = request.POST['title']
        )
        new_todo.save()
        return redirect('/')

    return render(request, 'index.html', {'todos':todo})


def delete(request,  pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')

def fire(request):

    name = database.child('Data').child('Name').get().val()
    age = database.child('Data').child('Age').get().val()

    return render(request, 'firebase.html', {
        "name":name,
        "age":age,
    })