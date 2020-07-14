from django.shortcuts import render
from .models import Feed, Nutrient, ExchangedFeed
from .serializers import FeedSerializer, NutrientSerializer
from rest_framework import viewsets 


class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

class NutrientViewSet(viewsets.ModelViewSet):
    queryset = Nutrient.objects.all()
    serializer_class = NutrientSerializer






def cal_g(data):
    mydata = float(data)
    # cal_data = mydata* 
    pass
    # return cal_data



# 사료환산 func
def exchange_feed(request):
    queryset = Feed.objects.all()

    for obj in queryset:
        print(obj.name)
        print(obj.types)
        print(float(obj.calorie))
        print(float(obj.moisture))
        print(float(obj.crude_protein))
        print(float(obj.crude_fat))
        print(float(obj.crude_fiber))
        print(float(obj.crude_ash))
        print(float(obj.calcium))
        print(float(obj.phosphorus)*1000)
    pass
