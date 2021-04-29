from django_filters import rest_framework as filters
from .models import House


class HouseFilter(filters.FilterSet):
    price_min = filters.NumberFilter(field_name="price", lookup_expr='gte')
    price_max = filters.NumberFilter(field_name="price", lookup_expr='lte')

    price_mq_min = filters.NumberFilter(field_name="price_mq", lookup_expr='gte')
    price_mq_max = filters.NumberFilter(field_name="price_mq", lookup_expr='lte')

    mq_min = filters.NumberFilter(field_name="mq", lookup_expr='gte')
    mq_max = filters.NumberFilter(field_name="mq", lookup_expr='lte')

    costs_min = filters.NumberFilter(field_name="costs", lookup_expr='gte')
    costs_max = filters.NumberFilter(field_name="costs", lookup_expr='lte')

    class Meta:
        model = House
        fields = '__all__'
