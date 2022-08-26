from django.db import models

from django.db import models


class BookModel(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    page_count = models.IntegerField()

    def __str__(self):
        return self.name