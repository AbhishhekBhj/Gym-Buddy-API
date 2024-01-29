from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Workout
from .serializer import WorkoutSerializer

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

        except:
            return Response({"status": 500, "message": "Internal Server Error"})


class WorkoutGetView(APIView):
    def get(self, request):
        try:
            # get the user from request
            user = request.user
            current_time = timezone.now()

            # check if user is a pro member

            if user.is_pro_member:
                # if pro send all data
                queryset = Workout.objects.all()

            else:
                # if not pro member get data from last 15 days

                fiteen_days_ago = current_time - datetime.timedelta(days=15)
                queryset = Workout.objects.filter(date__gte=fiteen_days_ago)
            serializer = WorkoutSerializer(queryset, many=True)
            return Response(
                {"status": 200, "message": "Workout data", "data": serializer.data}
            )

        except:
            return Response({"status": 500, "message": "Internal Server Error"})
