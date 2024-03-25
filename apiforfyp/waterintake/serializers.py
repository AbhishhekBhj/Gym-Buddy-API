from .models import WaterIntake
from rest_framework import serializers


class WaterIntakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterIntake
        fields = "__all__"
