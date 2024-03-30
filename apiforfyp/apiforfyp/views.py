from django.shortcuts import redirect, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import ForgetPasswordSerializer
from exercise.views import ExerciseView
from logworkout.views import WorkoutGetView
from waterintake.views import WaterIntakeGetView
from reminders.views import RemindersGetAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import check_password
from logmeasurements.views import BodyMeasurementListCreateView
from caloricintake.views import CaloricIntakeGetView
from rest_framework_simplejwt.views import TokenViewBase
from .serializers import TokenObtainLifetimeSerializer, TokenRefreshLifetimeSerializer
from users.models import CustomUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout
from users.email import send_forget_password_otp
from django.core.exceptions import ValidationError


class HomePageAPIView(APIView):
    """
    API view for the home page.

    This view retrieves data from various other views and combines them into a response dictionary.

    Methods:
    - get: Retrieves data from ExerciseView, WorkoutGetView, WaterIntakeGetView, RemindersGetAPIView,
           BodyMeasurementListCreateView, and CaloricIntakeGetView, and combines them into a response dictionary.
    """

    def get(self, request, user):
        """
        Retrieves data from ExerciseView, WorkoutGetView, WaterIntakeGetView, RemindersGetAPIView,
        BodyMeasurementListCreateView, and CaloricIntakeGetView, and combines them into a response dictionary.

        Parameters:
        - request: The HTTP request object.
        - user: The user object.

        Returns:
        - A Response object containing the combined response data and status code.
        """
        # Instantiate the ExerciseView and call its get method
        exercise_view = ExerciseView()
        exercise_data = exercise_view.get(request)

        # Instantiate the WorkoutGetView and call its get method
        workout_view = WorkoutGetView()
        workout_data = workout_view.post(request)

        # Instantiate the WaterIntakeGetView and call its get method
        water_intake_view = WaterIntakeGetView()
        water_intake_data = water_intake_view.get(request, user=user)

        reminder_view = RemindersGetAPIView()
        reminder_set_data = reminder_view.get(request, user=user)

        measuremnt_view = BodyMeasurementListCreateView()
        measurement_data = measuremnt_view.get(request, user=user)

        caloricintake_view = CaloricIntakeGetView()
        caloricintake_data = caloricintake_view.get(request, user=user)

        # Combine the data into a response dictionary
        response_data = {
            "exercise_data": exercise_data.data,
            "workout_data": workout_data.data,
            "water_intake_data": water_intake_data.data,
            "reminder_data": reminder_set_data.data,
            "measurement_data": measurement_data.data,
            "caloricintake_data": caloricintake_data.data,
        }

        # Return the combined response
        return Response({"data": response_data, "status": status.HTTP_200_OK})


class PasswordCheckAPIView(APIView):
    """
    API view for checking if a provided password matches the one in the database.
    Requires authentication.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request, user):
        provided_password = request.data.get("password")
        user = request.user

        # Check if the provided password matches the one in the database
        return Response(
            {
                "password_match": check_password(provided_password, user.password),
                "status": status.HTTP_200_OK,
            }
        )


class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user):
        provided_password = request.data.get("password")
        user = CustomUser.objects.get(username=user)

        if provided_password is None:
            return Response(
                {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": "Password not provided",
                }
            )

        if provided_password == user.password:
            return Response(
                {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": "New password cannot be same as old password",
                }
            )

            # hash before saving
        hashed_password = make_password(provided_password)
        # change the password
        user.password = hashed_password
        user.save()

        return Response(
            {
                "status": status.HTTP_200_OK,
                "message": "Password changed successfully",
            }
        )


class TokenObtainPairView(TokenViewBase):
    """
    Returns jwt token
    """

    serializer_class = TokenObtainLifetimeSerializer


class TokenRefreshView(TokenViewBase):
    """
    Renknews token with new expire time
    """

    serializer_class = TokenRefreshLifetimeSerializer


def home(request):
    return render(request, "home.html")


def logouts(request):
    logout(request)
    return redirect("custom_login")


class ForgotPasswordView(APIView):
    def post(self, request):
        try:
            email = request.data.get("email")
            serializer = ForgetPasswordSerializer(data=request.data)
            user = CustomUser.objects.get(email=email)

            if user:

                otp = send_forget_password_otp(email)
                return Response(
                    {
                        "status": status.HTTP_200_OK,
                        "message": "OTP sent successfully",
                        "data": {"otp": otp, "email": email},
                    }
                )

            else:
                return Response(
                    {
                        "status": status.HTTP_400_BAD_REQUEST,
                        "message": "User not found",
                    }
                )
        except CustomUser.DoesNotExist:
            return Response(
                {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": "User not found",
                }
            )

        except Exception as e:
            return Response(
                {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": "An error occurred",
                }
            )


class ChangePasswordWithOTPView(APIView):
    def patch(self, request):
        try:
            email = request.data.get("email")
            user = CustomUser.objects.get(email=email)
            password = request.data.get("password")

            if password is None:
                raise ValidationError("Password cannot be empty")

            user.password = make_password(password)
            user.save()

            return Response(
                {
                    "status": status.HTTP_200_OK,
                    "message": "Password changed successfully",
                }
            )

        except CustomUser.DoesNotExist:
            return Response(
                {
                    "status": status.HTTP_404_NOT_FOUND,
                    "message": "User not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        except ValidationError as e:
            return Response(
                {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": str(e),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception as e:
            return Response(
                {
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "An error occurred",
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
