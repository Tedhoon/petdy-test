from django.shortcuts import render
from django.http import HttpResponse
from .models import Feed, Nutrient, ExchangedFeed, ExchangedNutrient
from .serializers import FeedSerializer, NutrientSerializer, ExchangedFeedSerializer, ExchangedNutrientSerializer
from rest_framework import viewsets 


class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

class NutrientViewSet(viewsets.ModelViewSet):
    queryset = Nutrient.objects.all()
    serializer_class = NutrientSerializer


class ExchangedFeedViewSet(viewsets.ModelViewSet):
    queryset = ExchangedFeed.objects.all()
    serializer_class = ExchangedFeedSerializer

class ExchangedNutrientViewSet(viewsets.ModelViewSet):
    queryset = ExchangedNutrient.objects.all()
    serializer_class = ExchangedNutrientSerializer








# 사료환산 func
def exchange_feed(request):
    queryset = Feed.objects.all()

    for obj in queryset:
        ExchangedFeed.objects.create(
            name= obj.name,
            types = obj.types,
            calorie = round(float(obj.calorie)/100, 6),
            moisture = round(float(obj.moisture)/100, 6),
            crude_protein = round(float(obj.crude_protein)/100, 6),
            crude_fat = round(float(obj.crude_fat)/100, 6),
            crude_fiber = round(float(obj.crude_fiber)/100, 6),
            crude_ash = round(float(obj.crude_ash)/100, 6),
            calcium = round(float(obj.calcium)/100, 6),
            phosphorus = round(float(obj.phosphorus)/100, 6),
        )
        
        print(f"{obj.name} 오브젝트가 생성되었습니다.")
    return HttpResponse("환산이 완료되었습니다.")

# 영양소 환산 func
def exchange_nutrient(request):
    queryset = Nutrient.objects.all()

    for obj in queryset:
        ExchangedNutrient.objects.create(
            name= obj.name,
            calorie = round(float(obj.calorie)/100, 6),
            moisture = round(float(obj.moisture)/100, 6),
            crude_protein = round(float(obj.crude_protein)/100, 6),
            crude_fat = round(float(obj.crude_fat)/100, 6),
            crude_fiber = round(float(obj.crude_fiber)/100, 6),
            crude_ash = round(float(obj.crude_ash)/100, 6),
            calcium = round(float(obj.calcium)/100, 6),
            phosphorus = round(float(obj.phosphorus)/100, 6),
        )
        
        print(f"{obj.name} 오브젝트가 생성되었습니다.")
    return HttpResponse("환산이 완료되었습니다.")
