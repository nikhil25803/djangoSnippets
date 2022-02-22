from attr import fields
from django import forms
from matplotlib import widgets
from .models import Resume

GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

JOB_CITY = [
    ('Patna','Patna'),
    ('Ranchi','Ranchi'),
    ('Kolkata','Kolkata'),
    ('Wakanda','Wakanda'),
]

class ResumeForm(forms.ModelForm):

    gender = forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect)

    job_city = forms.MultipleChoiceField(label="Preffered Job City", choices=JOB_CITY, widget=forms.CheckboxSelectMultiple)

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
