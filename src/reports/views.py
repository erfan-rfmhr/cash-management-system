from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from transactions.models import TransactionModel
from transactions.serializers import TransactionSerializer


class AnnualReportView(ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = TransactionModel.objects.filter(user=self.request.user, date__year=self.kwargs['year'])
        return queryset
