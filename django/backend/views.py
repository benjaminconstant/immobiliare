from .models import House
from rest_framework import viewsets
from .serializers import HouseSerializer
from django.shortcuts import render
from .filters import HouseFilter


class HouseViewSet(viewsets.ModelViewSet):
    filterset_class = HouseFilter
    queryset = House.objects.all().order_by('-price')
    serializer_class = HouseSerializer
    http_method_names = ['get']


def index(request, path=''):
    return render(request, 'index.html')
