from rest_framework import viewsets 
from .models import AgeRange
from .serializers import AgeRangeSerializer
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response

class AgeRangeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AgeRange.objects.all()
    serializer_class = AgeRangeSerializer


class AgeRangeList(APIView):
    def get(self, request, format=None):
        queryset = AgeRange.objects.all()
        serializer = AgeRangeSerializer(queryset, many=True)
        return Response(serializer.data)
# Create your views here.
