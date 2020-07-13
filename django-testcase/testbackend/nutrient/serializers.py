from rest_framework import serializers
from .models import Nutrient, Feed

class FeedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Feed
        fields = '__all__'
        
class NutrientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Nutrient
        fields = '__all__'
         