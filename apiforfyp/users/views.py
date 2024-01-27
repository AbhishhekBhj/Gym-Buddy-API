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
from .serializers import ResendOTPSerializer, UserSerializer, OTPVerificationSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .email import *

# Create your views here.


# class UserRegistrationView(generics.CreateAPIView):
#     serializer_class = UserSerializer
#     permission_classes = [permissions.AllowAny]

#     def perform_create(self, serializer):
#         # Hash the password before saving the user
#         user = serializer.save()
#         user.set_password(serializer.validated_data["password"])
#         user.save()

#         return Response(
#             {"message": "User registered successfully"}, status=status.HTTP_201_CREATED
#         )


class UserRegistrationView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                send_otp(serializer.data["email"])
                return Response(
                    {
                        "status": 200,
                        "message": "User registered successfully",
                        "data": serializer.data,
                    }
                )

            return Response(
                {
                    "status": 400,
                    "message": "User registration failed",
                    "data": serializer.errors,
                }
            )

        except Exception as e:
            print(e)

            return Response(
                {
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "Internal Server Error",
                    "data": str(e),
                }
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


class VerifyOTPAPI(APIView):
    def post(self, request):
        try:
            serializer = OTPVerificationSerializer(data=request.data)

            if serializer.is_valid():
                email = serializer.data["email"]
                otp = serializer.data["otp"]

                user = CustomUser.objects.filter(email=email)
                if not user.exists():
                    return Response(
                        {
                            "status": 400,
                            "message": "Something went wrong",
                            "data": "invalid email",
                        }
                    )
                if user[0].otp != otp:
                    return Response(
                        {
                            "status": 400,
                            "message": "Something went wrong",
                            "data": "invalid otp",
                        }
                    )

                user = user.first()
                user.is_verified = True
                user.save()
                return Response(
                    {
                        "status": 200,
                        "message": "OTP verified successfully",
                        "data": (),
                    }
                )
        except Exception as e:
            print(e)
            return Response(
                {
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "Internal Server Error",
                    "data": str(e),
                }
            )


class ResendOTPView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = ResendOTPSerializer(data=data)
            if serializer.is_valid():
                email = serializer.data["email"]
                send_otp(email)
                return Response(
                    {
                        "status": 200,
                        "message": "OTP sent successfully",
                        "data": serializer.data,
                    }
                )
        except Exception as e:
            print(e)
            return Response(
                {
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "Internal Server Error",
                    "data": str(e),
                }
            )
