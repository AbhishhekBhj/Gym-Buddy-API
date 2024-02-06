from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from exercise.views import ExerciseView
from logworkout.views import WorkoutGetView
from waterintake.views import WaterIntakeGetView
from reminders.views import RemindersGetAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import check_password
from logmeasurements.views import BodyMeasurementListCreateView


class HomePageAPIView(APIView):
    def get(self, request, user):
        # Instantiate the ExerciseView and call its get method
        exercise_view = ExerciseView()
        exercise_data = exercise_view.get(request)

        # Instantiate the WorkoutGetView and call its get method
        workout_view = WorkoutGetView()
        workout_data = workout_view.get(request, user=user)

        # Instantiate the WaterIntakeGetView and call its get method
        water_intake_view = WaterIntakeGetView()
        water_intake_data = water_intake_view.get(request)

        reminder_view = RemindersGetAPIView()
        reminder_set_data = reminder_view.get(request, user=user)

        measuremnt_view = BodyMeasurementListCreateView()
        measurement_data = measuremnt_view.get(request, user=user)

        # Combine the data into a response dictionary
        response_data = {
            "exercise_data": exercise_data.data,
            "workout_data": workout_data.data,
            "water_intake_data": water_intake_data.data,
            "reminder_data": reminder_set_data.data,
            "measurement_data": measurement_data.data,
        }

        # Return the combined response
        return Response({"data": response_data, "status": status.HTTP_200_OK})


class PasswordCheckAPIView(APIView):
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
        user = request.user

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
        # change the password
        user.set_password(provided_password)
        user.save()

        return Response(
            {
                "status": status.HTTP_200_OK,
                "message": "Password changed successfully",
            }
        )
