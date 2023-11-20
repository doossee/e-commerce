from rest_framework import serializers
from .models import (
    Brand,
    Category,
)

class Brand(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class Category(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'