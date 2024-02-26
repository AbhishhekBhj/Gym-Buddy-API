from django.db import models


# Create your models here.
class Food(models.Model):
    food_name = models.CharField(max_length=100, default="Food Item", blank=False)
    food_image = models.ImageField(upload_to="food_images/", blank=True, null=True)
    food_description = models.CharField(
        max_length=1000, default="Food Description", blank=False
    )
    food_calories_per_serving = models.FloatField(default=0.0, blank=False)
    food_serving_size = models.FloatField(default=0.0, blank=False)
    food_protein_per_serving = models.FloatField(default=0.0, blank=False)
    food_carbs_per_serving = models.FloatField(default=0.0, blank=False)
    food_fat_per_serving = models.FloatField(default=0.0, blank=False)
    added_by_user = models.BooleanField(default=False)
    uploaded_by = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.food_name

    class Meta:
        db_table = "food_food"
