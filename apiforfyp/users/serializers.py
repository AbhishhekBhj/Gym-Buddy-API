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
            "height",
            "weight",
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


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ("username", "password")
        
        
        
class ForgetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        model = CustomUser
        fields = ("email",)
