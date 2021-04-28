from .models import House
from rest_framework import serializers


class HouseSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = House
        fields = '__all__'
