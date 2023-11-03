from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import TransactionModel


@receiver(post_save, sender=TransactionModel)
def update_balance(sender, instance, created, **kwargs):
    """Update user balance after transaction creation."""
    user = instance.user
    if created:
        user.balance += instance.amount if instance.type == 'income' else -instance.amount
    user.save()
