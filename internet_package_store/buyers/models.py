from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    wallet_balance = models.DecimalField(max_digits=10, decimal_places=2, default=100000)