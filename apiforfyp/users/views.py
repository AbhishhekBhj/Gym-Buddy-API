from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate, login
from .serializers import (
    ResendOTPSerializer,
    UserSerializer,
    OTPVerificationSerializer,
    LoginSerializer,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from .email import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password
from .models import CustomUser

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
                user = serializer.save()
                user.set_password(serializer.validated_data["password"])
                user.save()
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


# @csrf_exempt
# class LoginView(APIView):
#     authentication_classes = [TokenAuthentication]

#     @api_view(["POST"])
#     def post(self, request):
#         user = authenticate(
#             username=request.data["username"], password=request.data["password"]
#         )

#         if user:
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({"token": token.key})
#         else:
#             return Response(
#                 {"error": "Wrong Credentials"}, status=status.HTTP_404_NOT_FOUND
#             )


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


class LoginAPIView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data=data)
            if serializer.is_valid():
                username = serializer.data["username"]
                password = serializer.data["password"]
                authenticated_user = authenticate(username=username, password=password)

                if authenticated_user is None:
                    return Response(
                        {
                            "status": status.HTTP_400_BAD_REQUEST,
                            "message": "invalid credentials",
                            "data": {},
                        }
                    )

                if authenticated_user.is_verified == False:
                    return Response(
                        {
                            "status": status.HTTP_400_BAD_REQUEST,
                            "message": "Please verify your email first with the otp",
                            "data": {},
                        }
                    )

                refresh_token = RefreshToken.for_user(authenticated_user)
                login(request, authenticated_user)
                return Response(
                    {
                        "status": status.HTTP_200_OK,
                        "message": "Login Successful",
                        "data": {
                            "user_id": authenticated_user.id,
                            "name": authenticated_user.name,
                            "username": authenticated_user.username,
                            "age": authenticated_user.age,
                            "email": authenticated_user.email,
                            "fitness_level": authenticated_user.fitness_level,
                            "is_pro_member": authenticated_user.is_pro_member,
                            "fitness_goal": authenticated_user.fitness_goal,
                            "profile_picture": str(authenticated_user.profile_picture),
                        },
                        "refresh_token": str(refresh_token),
                        "access_token": str(refresh_token.access_token),
                    }
                )

            return Response(
                {
                    "status": 400,
                    "message": "Invalid Input",
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
