from rest_framework import serializers
from .models import CaloricIntake
from users.models import CustomUser
from food.models import Food


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username"]  # Add any other fields you want to include


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ["id", "food_name"]


class CaloricIntakeSerializers(serializers.ModelSerializer):

    username = CustomUserSerializer()
    food_consumed = FoodSerializer()

    class Meta:
        model = CaloricIntake
        fields = "__all__"
