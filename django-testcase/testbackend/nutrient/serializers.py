from rest_framework import serializers
from .models import Nutrient, Feed, Snack, ExchangedFeed, ExchangedNutrient, ExchangedSnack

class FeedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Feed
        fields = '__all__'
        
class NutrientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Nutrient
        fields = '__all__'
         
class SnackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snack
        fields = '__all__'

class ExchangedFeedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ExchangedFeed
        fields = '__all__'
        
class ExchangedNutrientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ExchangedNutrient
        fields = '__all__'

class ExchangedSnackSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExchangedSnack
        fields = '__all__'