from xml.etree.ElementInclude import include
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('',include('login_app.urls'))
]
