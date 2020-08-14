from django.shortcuts import render
# from rest_framework import viewsets 
from .serializers import MyPetSerializer 
from .models import MyPet
from rest_framework.views import APIView
from rest_framework.response import Response



class MyPetAPI(APIView):
    def get(self, request, format=None):
        queryset = MyPet.objects.all()
        serializer = MyPetSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MyPetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)