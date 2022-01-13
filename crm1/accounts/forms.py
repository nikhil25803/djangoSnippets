from attr import field
from django.forms import ModelForm
from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        # fields = ['customer']This would have fetched only customer from models.py