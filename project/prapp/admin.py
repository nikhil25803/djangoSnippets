from django.contrib import admin
from matplotlib.pyplot import cla

# Register your models here.

from  .models import Project


@admin.register(Project)
class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','college','year','prname','prdes','stack','lang','primg', 'repo', 'live', 'docs']
