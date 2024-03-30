import uuid
from django.db import models
from users.models import CustomUser

# Create your models here.

class PaymentHistory(models.Model):
    payment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)
    payment_description = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    
    
    def __str__(self):
        return str(self.payment_id)
