from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.index, name='homepage'),
    path('login/', views.logged_in, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout-page'),
    path('socoal-auth/', include('social_django.urls', namespace='social')),
]