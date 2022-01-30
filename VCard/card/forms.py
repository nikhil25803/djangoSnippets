from pyexpat import model
from attr import fields
from django.core import validators
from django import forms
from matplotlib import widgets
from .models import User

class register(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'twitter_name', 'username']
        widgets = {
            'first_name':forms.TextInput(),
            'last_name':forms.TextInput(),
            'email':forms.EmailInput(),
            'twitter_name':forms.TextInput(),
            'username':forms.TextInput(),
        }