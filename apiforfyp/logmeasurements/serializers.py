from rest_framework import serializers
from .models import BodyMeasurement


class LogMeasurementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyMeasurement
        fields = "__all__"
        
        
    
    