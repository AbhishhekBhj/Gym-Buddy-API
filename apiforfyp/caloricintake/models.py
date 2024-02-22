from django.db import models
from users.models import CustomUser
from food.models import Food

# Create your models here.


class CaloricIntake(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE, default=1)
    calories_consumed = models.FloatField(default=0.0)
    serving_consumed = models.FloatField(default=0.0)
    protein_consumed = models.FloatField(default=0.0)
    carbs_consumed = models.FloatField(default=0.0)
    fats_consumed = models.FloatField(default=0.0)
    timestamp = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["username", "timestamp"], name="composite_primary_key"
            )
        ]

    def __str__(self):
        return f"Caloric intake for {self.username} on {self.timestamp}"
