from django.http import HttpResponse


from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('cards/', views.cards),
    path('profile/', views.profiles),
    path('delete/<int:id>', views.delete, name="deletedata"),
]
