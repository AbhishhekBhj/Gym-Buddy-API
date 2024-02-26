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
from rest_framework.permissions import IsAuthenticated

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
    """
    View for user registration.

    This view handles the registration of new users by accepting a POST request with user data.
    Upon successful registration, an email with an OTP (One-Time Password) is sent to the user's email address.

    Methods:
    - post: Handles the POST request for user registration.
    """

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
    """
    API view for verifying OTP.

    Methods:
    - post: Verifies the OTP provided by the user.

    Attributes:
    - serializer: Instance of OTPVerificationSerializer class for validating the request data.
    - email: Email address extracted from the validated serializer data.
    - otp: OTP extracted from the validated serializer data.
    - user: Queryset of CustomUser objects filtered by email.
    """

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
    """
    API view for resending OTP.

    This view handles the POST request to resend the OTP (One-Time Password)
    to the specified email address. It expects the email address in the request
    data and sends the OTP to that email address using the `send_otp` function.

    If the request data is valid and the OTP is sent successfully, it returns
    a JSON response with a status code of 200, a success message, and the
    serialized data.

    If any exception occurs during the process, it returns a JSON response
    with a status code of 500, an error message, and the exception details.
    """

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
    """
    API view for user login.

    Methods:
    - post: Handles the POST request for user login.
    """

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
                            "weight": authenticated_user.weight,
                            "height": authenticated_user.height,
                            "gender": authenticated_user.gender,
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


class UploadProfilePicture(APIView):
    """
    API view for uploading a profile picture for a user.

    Methods:
    - post: Handles the POST request for uploading a profile picture.
    """

    def post(self, request, user):
        try:
            # Retrieve the user instance based on the username provided in the URL
            user_instance = CustomUser.objects.get(username=user)

            # Access the user's profile_picture field
            profile_picture = request.data.get("profile_picture")

            if profile_picture:
                # Update the profile_picture field of the user instance
                user_instance.profile_picture = profile_picture
                user_instance.save()

                return Response(
                    {
                        "status": 200,
                        "message": "Profile Picture uploaded successfully",
                        "data": {
                            "profile_picture": user_instance.profile_picture.url,  # Assuming profile_picture is a FileField
                        },
                    }
                )
            else:
                return Response(
                    {
                        "status": status.HTTP_400_BAD_REQUEST,
                        "message": "No profile picture provided",
                    }
                )

        except CustomUser.DoesNotExist:
            return Response(
                {
                    "status": status.HTTP_404_NOT_FOUND,
                    "message": "User not found",
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


class EditUserDetails(APIView):
    """
    API view for editing user details.

    Requires authentication.

    Methods:
    - patch: Update user details.
    """

    permission_classes = [IsAuthenticated]

    def patch(self, request, user):
        try:
            user_instance = CustomUser.objects.get(username=user)
            data = request.data
            serializer = UserSerializer(user_instance, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "status": 200,
                        "message": "User details updated successfully",
                        "data": serializer.data,
                    }
                )
            return Response(
                {
                    "status": 400,
                    "message": "User details update failed",
                    "data": serializer.errors,
                }
            )
        except CustomUser.DoesNotExist:
            return Response(
                {
                    "status": 404,
                    "message": "User not found",
                }
            )
        except Exception as e:
            return Response(
                {
                    "status": 500,
                    "message": "Internal Server Error",
                    "data": str(e),
                },
            )

class UserDeleteAccountView(APIView):
    """
    View for deleting a user account.
    """

    permission_classes = [IsAuthenticated]

    def delete(self, request, user):
        """
        Delete a user account.

        Args:
            request (HttpRequest): The HTTP request object.
            user (str): The username of the user to be deleted.

        Returns:
            Response: The response containing the status and message.
        """
        try:
            user_instance = CustomUser.objects.get(username=user)
            user_instance.delete()
            return Response(
                {
                    "status": 200,
                    "message": "User deleted successfully",
                }
            )
        except CustomUser.DoesNotExist:
            return Response(
                {
                    "status": 404,
                    "message": "User not found",
                }
            )
        except Exception as e:
            return Response(
                {
                    "status": 500,
                    "message": "Internal Server Error",
                    "data": str(e),
                },
            )