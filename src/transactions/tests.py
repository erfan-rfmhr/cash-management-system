from datetime import date

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from .models import TransactionModel


class TransactionViewSetTestCase(APITestCase):
    def setUp(self):
        user = get_user_model()
        self.user = user.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.transaction = TransactionModel.objects.create(user=self.user, amount=100.00, type='income',
                                                           category='salary', date=date.today())

    def test_get_transactions(self):
        response = self.client.get(reverse('transactions:transaction-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_transaction(self):
        data = {'amount': 200.00, 'type': 'expense', 'category': 'groceries', 'date': date.today(),
                'user': self.user.pk}
        response = self.client.post(reverse('transactions:transaction-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TransactionModel.objects.count(), 2)
