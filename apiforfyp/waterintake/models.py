from django.db import models
from users.models import CustomUser


# Create your models here.
class WaterIntake(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    volume = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.user} - {self.volume}ml"
