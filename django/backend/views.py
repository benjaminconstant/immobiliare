from .models import House
from rest_framework import viewsets
from .serializers import HouseSerializer
from django.shortcuts import render


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all().order_by('-price')
    serializer_class = HouseSerializer
    http_method_names = ['get']


def index(request, path=''):
    return render(request, 'index.html')
