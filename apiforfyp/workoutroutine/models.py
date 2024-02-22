from django.db import models
from users.models import CustomUser
from exercise.models import Exercise

# Create your models here.


class WorkoutRoutine(models.Model):
    routine_id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    routine_name = models.CharField(max_length=100, blank=False)
    exercises = models.ForeignKey(Exercise, related_name="exercises", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sets = models.IntegerField(blank=False, default=0)
    reps = models.IntegerField(blank=False, default=0)
    
    notes = models.TextField(
        blank=True, null=True, help_text="Additional notes or comments", default=""
    )

    class Meta:
        verbose_name = "Workout Routine"
        verbose_name_plural = "Workout Routines"

    def __str__(self):
        return f"Workout routine {self.routine_name} created by {self.created_by} on {self.created_at}"
