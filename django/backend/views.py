from .models import House, Search, Image
from rest_framework import viewsets
from .serializers import HouseSerializer, SearchSerializer, ImageSerializer
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


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all().order_by('-url')
    serializer_class = ImageSerializer
    http_method_names = ['get']


def index(request, path=''):
    return render(request, 'index.html')
