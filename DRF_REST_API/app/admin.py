from django.contrib import admin
class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
# Import the model
from .models import StudentModel

# Register the model
admin.site.register(StudentModel, StudentAdmin)