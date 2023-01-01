from django.db import models
from transaction.base import BaseModel

# Create your models here.

class Transaction(BaseModel):
    transaction_type = models.CharField(max_length=255, null=False, blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

