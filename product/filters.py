import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['title', 'weather_type']

    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")
    weather_type = django_filters.CharFilter(field_name="weather_type__weather", lookup_expr="icontains")
