from rest_framework import serializers
from .models import Nutrient, Feed, ExchangedNutrient, ExchangedFeed

class FeedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Feed
        fields = '__all__'
        
class NutrientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Nutrient
        fields = '__all__'
         

class ExchangedFeedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ExchangedFeed
        fields = '__all__'
        
class ExchangedNutrientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ExchangedNutrient
        fields = '__all__'
         