
from django.db.models import fields
from rest_framework import serializers
from .models import StudentModel

class StudentSerialzers(serializers.ModelSerializer):

    class Meta:
        model = StudentModel
        fields = ('name', 'department', 'roll')