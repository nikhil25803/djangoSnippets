from django.db.models import fields
from rest_framework import serializers
from .models import Item

class ItemSerializers(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('category', 'subcategory', 'name', 'amount')