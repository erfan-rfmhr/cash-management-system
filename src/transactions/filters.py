from django_filters import rest_framework as filters

from .models import TransactionModel


class TransactionFilter(filters.FilterSet):
    date = filters.DateFromToRangeFilter()

    class Meta:
        model = TransactionModel
        fields = ('date', 'type', 'category')
