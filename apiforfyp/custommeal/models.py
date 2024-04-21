from django.db import models

# Create your models here.
from django.db import models
from users.models import CustomUser
from food.models import Food


from django.db import models


class MealType(models.Model):
    MEAL_TYPES = [
        ("Breakfast", "Breakfast"),
        ("Lunch", "Lunch"),
        ("Dinner", "Dinner"),
        ("Snacks", "Snacks"),
    ]
    name = models.CharField(max_length=20, choices=MEAL_TYPES, unique=True)

    def __str__(self):
        return self.name


class MealPlan(models.Model):
    PLAN_CHOICES = [
        ("Breakfast", "Breakfast"),
        ("Lunch", "Lunch"),
        ("Dinner", "Dinner"),
        ("Snack", "Snack"),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    meal_type = models.CharField(max_length=20, choices=PLAN_CHOICES)
    foods = models.ManyToManyField(Food, through="MealPlanFood")

    def __str__(self):
        return f"{self.user}'s {self.meal_type}"

    class Meta:
        db_table = "food_mealplan"


class MealUser(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    meal_type = models.ForeignKey(MealType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s {self.meal_type}"

    class Meta:
        unique_together = ('user', 'meal_type')

class MealPlanFood(models.Model):
    meal_plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    servings = models.FloatField(default=1.0)

    def __str__(self):
        return f"{self.food} - {self.servings} servings"

    class Meta:
        db_table = "food_mealplanfood"
