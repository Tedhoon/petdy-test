from django.shortcuts import render
from django.http import HttpResponse
from .models import Feed, Nutrient, Snack, ExchangedFeed, ExchangedNutrient, ExchangedSnack
from .serializers import FeedSerializer, NutrientSerializer, SnackSerializer, ExchangedFeedSerializer, ExchangedNutrientSerializer ,ExchangedSnackSerializer
from rest_framework import viewsets 


class FeedViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

class NutrientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Nutrient.objects.all()
    serializer_class = NutrientSerializer

class SnackViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer

class ExchangedFeedViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ExchangedFeed.objects.all()
    serializer_class = ExchangedFeedSerializer

class ExchangedNutrientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ExchangedNutrient.objects.all()
    serializer_class = ExchangedNutrientSerializer

class ExchangedSnackViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ExchangedSnack.objects.all()
    serializer_class = ExchangedSnackSerializer








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

# 간식 환산 func
def exchange_snack(request):
    queryset = Snack.objects.all()

    for obj in queryset:
        ExchangedSnack.objects.create(
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
