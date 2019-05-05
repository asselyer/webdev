from django_filters import rest_framework as filters
from api.models import Task


class TaskFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')
    release_year = filters.NumberFilter(field_name='due_on', lookup_expr='year')
    release_year__gt = filters.NumberFilter(field_name='due_on', lookup_expr='year__gt')
    release_year__lt = filters.NumberFilter(field_name='due_on', lookup_expr='year__lt')

 
    class Meta:
        model = Task
        fields = ('name', 'status', 'due_on')