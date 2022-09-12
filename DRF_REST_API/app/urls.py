from django.urls import path
from . import views

urlpatterns = [
    path('', views.Overview, name='about'),
    
    # Endpoint for POST method
    path('add/', views.addStudent, name='add-student'),
]