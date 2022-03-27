# from email import contentmanager
# from pyexpat import model
from django.db import models
# from matplotlib.pyplot import title
from django.utils import timezone
from django.contrib.auth.models import User

# Post model

class Post(models.Model):

    title = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

