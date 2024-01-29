from django.db import models

from django.utils import timezone
from users.models import CustomUser
from exercise.models import Exercise
import uuid


# Create your models here.
class Workout(models.Model):
    workout_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    exercise_id = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=False)
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)
    started_at = models.DateField(default=timezone.now)
    ended_at = models.DateField(default=timezone.now)
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(default=timezone.now)
    sets = models.IntegerField(null=False)
    reps = models.IntegerField(null=False)
    weight = models.IntegerField(null=False)
    volume = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.username}s Workout on {self.started_at}"
