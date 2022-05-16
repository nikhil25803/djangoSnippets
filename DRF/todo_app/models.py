from django.db import models

# Create your models here.

class Item(models.Model):

    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    amounts = models.PositiveBigIntegerField()

    def __str__(self):
        return self.name