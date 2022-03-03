from pyexpat import model
from statistics import mode
from django.db import models
from matplotlib.image import thumbnail
from matplotlib.pyplot import title

# Create your models here.

class Book(models.Model):

    title = models.CharField(max_length=256)
    pageCount = models.IntegerField(default=0)
    thumbnailURL = models.CharField(max_length=256,null=True)
    shortDescription = models.CharField(max_length=256, null=True)
    longDescription = models.TextField(null=True)

