from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Workout
from .serializer import WorkoutSerializer
from users.models import CustomUser

from django.utils import timezone
import datetime

# Create your views here.


class WorkoutView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = WorkoutSerializer(data=data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "status": 201,
                        "message": "Workout added successfully",
                        "data": serializer.data,
                    }
                )
            else:
                return Response(
                    {
                        "status": 400,
                        "message": "Error Adding Workout",
                        "data": serializer.errors,
                    }
                )

        except AssertionError as e:
            return Response(
                {
                    "status": 400,
                    "message": "Bad Request",
                    "error": e,
                }
            )
        except Exception as e:
            return Response(
                {"status": 500, "message": "Internal Server Error", "error": e}
            )


class WorkoutGetView(APIView):
    def post(self, request):
        try:
            # Assuming you're passing user ID in the request data
            user_id = request.data.get("user_id")

            # Retrieve the CustomUser object using the user_id
            user = CustomUser.objects.get(id=user_id)
            current_time = timezone.now()

            # check if user is a pro member
            if user.is_pro_member:
                # if pro send all data sorted by date
                queryset = (
                    Workout.objects.filter(username=user).order_by("-created_at").all()
                )
            else:
                # if not pro member get data from the last 15 days sorted by date
                fifteen_days_ago = current_time - datetime.timedelta(days=15)
                queryset = Workout.objects.filter(
                    username=user, created_at__gte=fifteen_days_ago
                ).order_by("-created_at")

            serializer = WorkoutSerializer(queryset, many=True)
            return Response(
                {
                    "status": 200,
                    "message": "Workout data retrieved successfully",
                    "data": serializer.data,
                }
            )
        except Exception as e:
            # Handle exceptions more explicitly for debugging purposes
            return Response(
                {"status": 500, "message": "Internal Server Error", "error": str(e)}
            )


class WorkoutObjectDeleteView(APIView):
    def delete(self, request):
        try:
            workout_id = request.data.get("workout_id")

            if workout_id:
                workout_object = Workout.objects.get(workout_id=workout_id)
                workout_object.delete()

                return Response(
                    {
                        "status": 200,
                        "message": "Workout deleted successfully",
                    }
                )

            else:
                return Response(
                    {
                        "status": 400,
                        "message": "Workout ID not provided",
                    }
                )

        except Exception as e:
            return Response(
                {
                    "status": 500,
                    "message": "Internal Server Error",
                    "error": str(e),
                }
            )
