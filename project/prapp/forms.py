from distutils.command.build_scripts import first_line_re
from attr import field
from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name','college','year','prname','prdes','stack','lang','primg', 'repo', 'live', 'docs']