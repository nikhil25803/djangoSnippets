from django.http import HttpResponse
from django.shortcuts import render
import json


booksData = open('J:/Programming/Git & GitHub/Django_File0/Django_Docs/bookstore/books.json').read()

data = json.loads(booksData)

# Create your views here.

def index(request):
    context = {'books':data}
    return render(request, 'books/html/index.html', context)


def show(request, id):
    singleBook = ()

    for book in data:
        if book['id'] == id:
            singleBook= book

    context = {'book':singleBook}
    return render(request, 'books/html/show.html', context)
