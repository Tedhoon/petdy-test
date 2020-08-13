from rest_framework import serializers
from .models import AgeRange

class AgeRangeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AgeRange
        fields = '__all__'