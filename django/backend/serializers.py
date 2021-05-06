from .models import House, Search, Image
from rest_framework import serializers


class SearchSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Search
        fields = '__all__'


class ImageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Image
        fields = ['url']


class HouseSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    searches = SearchSerializer(many=True, read_only=True)
    image_set = ImageSerializer(many=True)

    class Meta:
        model = House
        fields = '__all__'
