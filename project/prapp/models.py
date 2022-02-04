from distutils.command.upload import upload
from django.db import models
from django.forms import IntegerField
from django.utils import timezone

# Create your models here.
# Below code could be used if only one choice is need to be chosen
STACK = [
    ('Frontend','Frontend'),
    ('Backend','Backend'),
    ('UI/UX','UI/UX'),
    ('Full Stack','Full Stack'),
    ('Android','Android'),
    ('Flutter','Flutter'),
    ('Other','Other'),

]

# LANGUAGES = [
#     ('HTML','HTML'),
#     ('CSS','CSS'),
#     ('JavaScript','JavaScript'),
#     ('Python','Python'),
#     ('Java','Java'),
#     ('C++','C++'),
#     ('C','C'),
#     ('C#','C#'),
#     ('PHP','PHP'),
#     ('SQL','SQL'),
#     ('Swift','Swift'),
#     ('Other','Other'),

# ]



class Project(models.Model):
    name = models.CharField(max_length=50)

    college = models.CharField(max_length=100)

    # year = models.PositiveIntegerField()

    #dou = models.DateField(default=timezone.now)

    prname = models.CharField(max_length=50)

    prdes = models.CharField(max_length=100)

    stack = models.CharField(max_length=100, choices=STACK)

    lang = models.CharField(max_length=100) # Choices to be added

    primg = models.ImageField(upload_to='primg', blank=True)

    repo = models.CharField(max_length=100)

    live = models.CharField(max_length=100,null=True)

    docs = models.CharField(max_length=100,null=True)



