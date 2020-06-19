from django.db import models
from datetime import date


# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=64, blank=False)
    account_created = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.name}"


class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='accounts')
    cash_in = models.FloatField(default=0)
    cash_out = models.FloatField(default=0)
    transaction_added = models.DateField(default=date.today)
    particular = models.TextField(blank=True)
