import django_filters
from .models import Fooditem

class FooditemFilter(django_filters.FilterSet):
    class Meta:
        model = Fooditem
        fields = ['name']