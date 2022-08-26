# app/views.py
from rest_framework import viewsets
from .models import BookModel
from .serializers import BookSerializer

class BookList(viewsets.ModelViewSet):

    queryset = BookModel.objects.all()
    serializer_class = BookSerializer