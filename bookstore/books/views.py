from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
import json
from books.models import Book


# Create your views here.

def index(request):
    dbData = Book.objects.all()
    context = {'books':dbData}
    return render(request, 'books/html/index.html', context)


def show(request, id):

    singleBook = get_object_or_404(Book, pk=id)

    context = {'book':singleBook}
    return render(request, 'books/html/show.html', context)

def review(request):

    return redirect('/book')
