from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class TransactionModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
