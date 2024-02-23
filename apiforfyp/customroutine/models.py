from django.db import models
from users.models import CustomUser
from exercise.models import Exercise

# Create your models here


class Routine(models.Model):
    routine_id = models.AutoField(primary_key=True)
    exericse = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.IntegerField(default=1)
    reps = models.IntegerField(default=1)
    weight = models.IntegerField(default=1)
    notes = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Routine created with {self.exericse}"


class CustomRoutine(models.Model):
    custom_routine_id = models.AutoField(primary_key=True)
    routine = models.ManyToManyField(Routine)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.created_by}'s custom routine created at {self.created_at}"
