from django.urls import path

from django import views

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:id>', views.show),
]