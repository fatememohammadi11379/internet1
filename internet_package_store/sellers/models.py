from django.db import models

class Seller(models.Model):
    name = models.CharField(max_length=100)
    is_approved = models.BooleanField(default=False)
