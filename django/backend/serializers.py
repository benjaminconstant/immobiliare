from .models import House, Search
from rest_framework import serializers


class SearchSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Search
        fields = '__all__'


class HouseSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    searches = SearchSerializer(many=True, read_only=True)

    class Meta:
        model = House
        fields = '__all__'
