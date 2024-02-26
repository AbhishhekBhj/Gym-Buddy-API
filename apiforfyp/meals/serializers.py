from rest_framework.serializers import ModelSerializer

from .models import CustomMeal


class CustomMealSerializer(ModelSerializer):
    class Meta:
        model = CustomMeal
        fields = "__all__"
