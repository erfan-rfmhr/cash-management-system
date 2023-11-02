from rest_framework.serializers import ModelSerializer

from .models import TransactionModel


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = TransactionModel
        fields = ('user', 'amount', 'type', 'category', 'date')
