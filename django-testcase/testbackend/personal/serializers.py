from rest_framework import serializers
from .models import MyPet
from datas.models import DogBreed
class MyPetSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyPet
        fields = '__all__'

    # def save(self, validated_data):
    #     print(validated_data)
        # self.breed = DogBreed.objects.get(id=1)