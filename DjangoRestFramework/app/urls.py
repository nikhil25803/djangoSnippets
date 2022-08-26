# app/urls.py

from django.urls import path, include
from rest_framework import routers
from app.views import BookList


router = routers.DefaultRouter()
router.register(r'books', BookList)

urlpatterns = [
    path('', include(router.urls)),
]
