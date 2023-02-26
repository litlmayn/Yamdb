from django_filters.rest_framework import CharFilter, FilterSet

from titles.models import Title


class TitleFilter(FilterSet):
    genre = CharFilter(field_name='genres__slug',)
    category = CharFilter(field_name='categories__slug',)
    name = CharFilter(field_name='name', lookup_expr='contains',)