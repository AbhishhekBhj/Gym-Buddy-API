from django.shortcuts import render
from reminders.models import Reminder
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReminderSerializer
from rest_framework.views import APIView


class RemindersSetAPIView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = ReminderSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "message": "Reminder set successfully",
                        "data": serializer.data,
                        "status": status.HTTP_201_CREATED,
                    }
                )
            else:
                return Response(
                    {
                        "message": "Reminder not set",
                        "data": serializer.errors,
                        "status": status.HTTP_400_BAD_REQUEST,
                    }
                )

        except Exception as e:
            return Response(
                {
                    "message": "Reminder not set",
                    "data": str(e),
                    "status": status.HTTP_400_BAD_REQUEST,
                }
            )


class RemindersGetAPIView(APIView):
    def get(self, request):
        try:
            reminders = Reminder.objects.all()
            serializer = ReminderSerializer(reminders, many=True)
            return Response(
                {
                    "message": "Reminders fetched successfully",
                    "data": serializer.data,
                    "status": status.HTTP_200_OK,
                }
            )
        except Exception as e:
            return Response(
                {
                    "message": "Reminders not fetched",
                    "data": str(e),
                    "status": status.HTTP_400_BAD_REQUEST,
                }
            )
