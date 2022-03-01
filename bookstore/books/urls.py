from django.urls import path

from django import views

from . import views

urlpatterns = [
    path('', views.index, name='book.all'),
    path('<int:id>', views.show, name="book.show"),
]