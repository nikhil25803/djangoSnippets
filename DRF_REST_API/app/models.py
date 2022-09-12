from django.db import models

class StudentModel(models.Model):

    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    roll = models.IntegerField()

    def __str__(self) -> str:
        return self.name