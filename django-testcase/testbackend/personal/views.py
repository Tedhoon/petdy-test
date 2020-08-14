from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import MyPetSerializer 
from .models import MyPet


class MyPetViewSet(viewsets.ModelViewSet):
    queryset = MyPet.objects.all()
    serializer_class = MyPetSerializer