from django.contrib import admin

# Import the model
from .models import StudentModel

# Register the model
admin.site.register(StudentModel)