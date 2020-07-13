from django.shortcuts import render
from .models import Feed, Nutrient
from .serializers import FeedSerializer, NutrientSerializer
from rest_framework import viewsets 


class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

class NutrientViewSet(viewsets.ModelViewSet):
    queryset = Nutrient.objects.all()
    serializer_class = NutrientSerializer