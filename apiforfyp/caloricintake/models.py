from django.db import models
from users.models import CustomUser

# Create your models here.


class CaloricIntake(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    calories_consumed = models.FloatField(default=0.0)
    serving_consumed = models.FloatField(default=0.0)
    protein_consumed = models.FloatField(default=0.0)
    carbs_consumed = models.FloatField(default=0.0)
    fats_consumed = models.FloatField(default=0.0)
    timestamp = models.DateTimeField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["username", "timestamp"], name="composite_primary_key"
            )
        ]
