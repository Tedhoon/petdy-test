from django.shortcuts import render
# from rest_framework import viewsets 
from .serializers import MyPetSerializer 
from .models import MyPet
from datas.models import DogBreed
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q


class MyPetAPI(APIView):
    def get(self, request, format=None):
        queryset = MyPet.objects.all()
        serializer = MyPetSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print(request.data)
        serializer = MyPetSerializer(data=request.data)

        if serializer.is_valid():
            mypet = ''
            try:
                mypet = MyPet.objects.get(
                        Q(owner=request.data['owner']) & 
                        Q(name=request.data['name'])
                        )
            except:
                pass
                
            if mypet:
                # qs가 있으면 수정으로 적용
                mypet.owner = request.data['owner']
                mypet.name = request.data['name']
                mypet.age = request.data['age']
                mypet.weight = request.data['weight']
                mypet.save()
            else:
                # 없으면 object create
                serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)