from django.db import models
from users.models import CustomUser
# Create your models here.

class CustomMeal(models.Model):
    meal_id = models.AutoField(primary_key=True)
    meal_name = models.CharField(max_length=100, default="Meal Item", blank=False)
    meal_image = models.ImageField(upload_to="meal_images/", blank=True, null=True)
    meal_description = models.CharField(
        max_length=1000, default="Meal Description", blank=False
    )
    meal_calories = models.FloatField(default=0.0, blank=False)
    meal_protein = models.FloatField(default=0.0, blank=False)
    meal_carbs = models.FloatField(default=0.0, blank=False)
    meal_fat = models.FloatField(default=0.0, blank=False)
    added_by_user = models.BooleanField(default=False)
    uploaded_by = models.ForeignKey(CustomUser, blank=True, null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.meal_name

    class Meta:
        db_table = "food_meal"