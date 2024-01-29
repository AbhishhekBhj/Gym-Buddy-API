from django.db import models
from users.models import CustomUser
import uuid

# Create your models here.


class Meditation(models.Model):
    meditation_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)
    meditation_date = models.DateField()
    meditation_duration = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.username}'s Meditation on {self.meditation_date}"
