from .models import House, Search
from rest_framework import viewsets
from .serializers import HouseSerializer, SearchSerializer
from django.shortcuts import render
from .filters import HouseFilter


class HouseViewSet(viewsets.ModelViewSet):
    filterset_class = HouseFilter
    queryset = House.objects.all().order_by('-price')
    serializer_class = HouseSerializer
    http_method_names = ['get', 'put']


class SearchViewSet(viewsets.ModelViewSet):
    queryset = Search.objects.all().order_by('-name')
    serializer_class = SearchSerializer
    http_method_names = ['get']


def index(request, path=''):
    return render(request, 'index.html')
