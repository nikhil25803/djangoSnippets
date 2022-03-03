from django.http import HttpResponse
from django.shortcuts import render
import json
from books.models import Book


# Create your views here.

def index(request):
    dbData = Book.objects.all()
    context = {'books':dbData}
    return render(request, 'books/html/index.html', context)


def show(request, id):
    singleBook = Book.objects.get(pk=id)

    context = {'book':singleBook}
    return render(request, 'books/html/show.html', context)
