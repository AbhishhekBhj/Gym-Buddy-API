from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)

from rest_framework_simplejwt.tokens import RefreshToken


class TokenObtainLifetimeSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        
        data["lifetime"] = int(refresh.access_token.lifetime.total_seconds())
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "lifetime": data["lifetime"],
        }


class TokenRefreshLifetimeSerializer(TokenRefreshSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = RefreshToken(attrs["refresh"])
        data["lifetime"] = int(refresh.access_token.lifetime.total_seconds())
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "lifetime": data["lifetime"],
        }
