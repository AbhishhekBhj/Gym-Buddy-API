from django.db import models


class TargetBodyPart(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    exercise_id = models.AutoField(primary_key=True)
    exercise_name = models.CharField(max_length=100, blank=False)
    exercise_details = models.TextField()
    exercise_image = models.ImageField(
        upload_to="exercise_images/", blank=True, null=True
    )
    target_body_part = models.ManyToManyField(TargetBodyPart)

    def __str__(self):
        return self.exercise_name