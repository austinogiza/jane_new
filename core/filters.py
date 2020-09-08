import django_filters
from .models import Item


class ProductFilter(django_filters.Filter):
    class Meta:
        model = Item
        fields = {
            'title': ['icontains']
        }

