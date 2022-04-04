
# from django import views
from unicodedata import name
from . import views
from django.urls import path



urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('firebase/', views.fire, name='fire'),
]