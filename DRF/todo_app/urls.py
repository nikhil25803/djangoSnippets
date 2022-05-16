from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='homepage'),
    path('api/', views.ApiOverview, name='api'),
    path('api/create/', views.add_items, name='api-add'),
    path('api/all/', views.view_items, name='api-view'),
]