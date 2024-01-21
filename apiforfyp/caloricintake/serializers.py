from rest_framework import serializers
from .models import CaloricIntake


class CaloricIntakeSerializers(serializers.ModelSerializer):
    class Meta:
        model = CaloricIntake
        fields = "__all__"
