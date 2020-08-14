from rest_framework import serializers
from .models import MyPet

class MyPetSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyPet
        fields = '__all__'