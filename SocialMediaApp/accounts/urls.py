
from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signup/', views.signup_view, name='signup-page'),
    path('login/', views.login_view, name='login-page'),
]