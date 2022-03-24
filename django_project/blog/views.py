# import imp
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author': 'Nikhil Raj',
        'title': 'Blog Post 1',
        'content': 'My first blog post',
        'date_posted': 'August 20, 2020',
    },

    {
        'author': 'Nikhil Raj 02',
        'title': 'Blog Post 02',
        'content': 'My Second blog post',
        'date_posted': 'August 20, 2021',
    },
    {
        'author': 'Nikhil Raj 03',
        'title': 'Blog Post 03',
        'content': 'My Second blog post',
        'date_posted': 'August 20, 2021',
    },


]

def home(request):

    context = {
        'posts': posts,
    }

    return render(request, 'blog/index.html', context)

def about(request):

    return render(request, 'blog/about.html', {'title':'About'})

