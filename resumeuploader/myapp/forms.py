from attr import fields
from django import forms
from matplotlib import widgets
from .models import Resume


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'dob', 'gender', 'locality', 'city', 'pin',
                  'state', 'mobile', 'job_city', 'profile_image', 'my_file']

        labels = {'name': 'Full Name', 'dob': 'Date of Birth', 'pin': 'Pin Code', 'mobile': 'Mobile No',
                  'email': 'Email ID', 'profile_iamge': 'Profile Image', 'my_file': 'Documents'}

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            
            'dob': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker'}),
            
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            
            'pin': forms.NumberInput(attrs={'class': 'form-control'}),
            
            'state': forms.Select(attrs={'class': 'form-select'}),
            
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            

        }
