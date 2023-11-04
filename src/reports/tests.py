from datetime import date

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from transactions.models import TransactionModel


class ReportViewTestCase(APITestCase):
    def setUp(self):
        user = get_user_model()
        self.user = user.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.transaction = TransactionModel.objects.create(user=self.user, amount=100.00, type='income',
                                                           category='salary', date=date.today())

    def test_annual_report(self):
        response = self.client.get(reverse('reports:annual-report', kwargs={'year': date.today().year}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_monthly_report(self):
        response = self.client.get(
            reverse('reports:monthly-report', kwargs={'year': date.today().year, 'month': date.today().month}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_daily_report(self):
        response = self.client.get(
            reverse('reports:daily-report', kwargs={'year': date.today().year, 'month': date.today().month,
                                                    'day': date.today().day}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
