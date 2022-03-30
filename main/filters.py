import django_filters
from dashboard.models import *


class CustomSearchMedicine(django_filters.FilterSet):
    class Meta:
        model = Medicine
        fields = ['medicine_name','comapny']