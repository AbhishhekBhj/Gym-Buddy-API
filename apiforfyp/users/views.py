from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework import generics, permissions
from .serializers import UserSerializer
from rest_framework.decorators import api_view

# Create your views here.


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        # Hash the password before saving the user
        user = serializer.save()
        user.set_password(serializer.validated_data["password"])
        user.save()

        return Response(
            {"message": "User registered successfully"}, status=status.HTTP_201_CREATED
        )


@csrf_exempt
class LoginView(APIView):
    authentication_classes = [TokenAuthentication]

    @api_view(["POST"])
    def post(self, request):
        user = authenticate(
            username=request.data["username"], password=request.data["password"]
        )

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        else:
            return Response(
                {"error": "Wrong Credentials"}, status=status.HTTP_404_NOT_FOUND
            )
