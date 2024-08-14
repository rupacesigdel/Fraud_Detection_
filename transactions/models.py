from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
    merchant = models.CharField(max_length=255)
    is_fraudulent = models.BooleanField(default=False)

    def __str__(self):
        return f"Transaction {self.id} by {self.user.username}"
