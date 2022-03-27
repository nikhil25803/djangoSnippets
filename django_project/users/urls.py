# from unicodedata import name
from django.urls import path
from . import views
# import users

urlpatterns = [
    path('register/', views.register, name='register'),
]