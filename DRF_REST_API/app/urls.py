
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Overview, name='about'),
    # Endpoint for POST method
    path('add/', views.addStudent, name='add-student'),
    # Endpoint for PUT method
    path('update/<int:pk>', views.update, name='update'),
    # Endpoint for PATCH method
    path('modify/<int:pk>', views.modify, name='update-element'),
    # Endpoint for GET method
    path('listStudents/', views.listStudents, name='list-students'),
    # Endpoint for DELETE method
    path('remove/<int:pk>', views.removeStudent, name='remove-student')
]