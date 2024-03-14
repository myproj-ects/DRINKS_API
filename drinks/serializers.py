from rest_framework import serializers
from .models import Drink

# Serializer class for the Drink model
class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        # Meta class to define metadata options for the serializer
        model = Drink  # Specify the model to be serialized
        fields = ['id', 'name', 'description']  # Specify the fields to include in the serialization