from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "name",
            "age",
            "email",
            "password",
            "fitness_level",
            "fitness_goal",
            "is_verified",
        )


class OTPVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ("email", "otp")


class ResendOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        model = CustomUser
        fields = ("email",)
