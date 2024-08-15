from django.db import models

class Transaction(models.Model):
    transaction_id = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    merchant = models.CharField(max_length=255)
    is_fraud = models.BooleanField(default=False)

    def __str__(self):
        return self.transaction_id
