from pyexpat import model
from statistics import mode
from django.db import models
from matplotlib.pyplot import title

# Create your models here.

class Book(models.Model):

    title = models.CharField(max_length=100)
