from food.serializers import FoodSerializer
from rest_framework import serializers
from .models import MealPlan


class MealPlanSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(many=True, read_only=True)

    class Meta:
        model = MealPlan
        fields = "__all__"
