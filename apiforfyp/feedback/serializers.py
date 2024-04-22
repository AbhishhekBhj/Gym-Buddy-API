from rest_framework import serializers
from .models import FeedBack

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = "__all__"