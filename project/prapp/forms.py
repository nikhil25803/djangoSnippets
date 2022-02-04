from distutils.command.build_scripts import first_line_re
from attr import field
from django import forms
from matplotlib import widgets
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name','college','prname','prdes','stack','lang','primg', 'repo', 'live', 'docs']

        labels = {'name':'Name of the Studets','college':'College Name', 'year':'Year', 'prname':'Project Name', 'prdes':'Project Description', 'stack':'Tech Stack Used', 'lang':'Language Used', 'primg':'Project Image', 'repo':'GitHub Repo Link','live':'Live Link', 'docs':'Documentation'}

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),

            'college':forms.TextInput(attrs={'class':'form-control'}),

            'prname':forms.TextInput(attrs={'class':'form-control'}),

            'prdes':forms.TextInput(attrs={'class':'form-control'}),

            'repo':forms.TextInput(attrs={'class':'form-control'}),

            'live':forms.TextInput(attrs={'class':'form-control'}),

            'docs':forms.TextInput(attrs={'class':'form-control'}),


        }