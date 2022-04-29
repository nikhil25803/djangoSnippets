
from django import forms
from .models import AmountModel

class AmountForm(forms.ModelForm):

    class Meta:
        model = AmountModel

        fields = ['name', 'amount']