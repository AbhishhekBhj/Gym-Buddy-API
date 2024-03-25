from datetime import timedelta, timezone
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import BodyMeasurement
from .serializers import LogMeasurementsSerializer
from users.models import CustomUser
import datetime
from django.utils import timezone


class BodyMeasurementListCreateViewPro(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = LogMeasurementsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                {
                    "status": status.HTTP_201_CREATED,
                    "message": "Measurement added successfully",
                    "data": serializer.data,
                }
            )

        return Response(
            {
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Measurement could not be added",
                "data": serializer.errors,
            }
        )


class BodyMeasurementListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user):
        user = request.user
        try:
            measurement = BodyMeasurement.objects.filter(user=user).all()
            serializer = LogMeasurementsSerializer(measurement, many=True)
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

    def post(self, request, format=None):
        serializer = LogMeasurementsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                {
                    "status": status.HTTP_201_CREATED,
                    "message": "Measurement added successfully",
                    "data": serializer.data,
                }
            )

        return Response(
            {
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Measurement could not be added",
                "data": serializer.errors,
            }
        )


class BodyMeasurementDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):

        try:
            user_id = request.data.get("user_id")

            try:
                user = CustomUser.objects.get(id=user_id)
            except CustomUser.DoesNotExist:
                return Response(
                    {
                        "status": 404,
                        "message": "User not found",
                    }
                )

            current_time = timezone.now()

            if user.is_pro_member:
                queryset = BodyMeasurement.objects.filter(user=user).all()
            else:
                fifteen_days_ago = current_time - datetime.timedelta(days=15)
                queryset = BodyMeasurement.objects.filter(
                    user=user, created_at__gte=fifteen_days_ago
                )

            serializer = LogMeasurementsSerializer(queryset, many=True)
            return Response(
                {
                    "status": 200,
                    "message": "Measurement data retrieved successfully",
                    "data": serializer.data,
                }
            )

        except AttributeError as e:
            error_message = str(e)  # Extract the error message from AttributeError
            return Response(
                {
                    "status": 400,
                    "message": "Bad Request",
                    "error": error_message,
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

        # user_id = request.data.get("user_id")
        # user = get_object_or_404(CustomUser, id=user_id)
        # is_pro_member = user.is_pro_member

        # if is_pro_member or user == request.user:
        #     if is_pro_member:
        #         queryset = BodyMeasurement.objects.filter(user=user)
        #     else:
        #         # Show measurements of the last 15 days
        #         queryset = BodyMeasurement.objects.filter(
        #             user=user, created_at__gte=timezone.now() - timedelta(days=15)
        #         )

        #     serializer = LogMeasurementsSerializer(queryset, many=True)
        #     return Response(serializer.data)
        # else:
        #     return Response(
        #         {"detail": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN
        #     )


class BodyMeasurementObjectEditView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, measurement_id):
        measurement_instance = get_object_or_404(BodyMeasurement, id=measurement_id)
        data = request.data

        serializer = LogMeasurementsSerializer(
            measurement_instance, data=data, partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Measurement details edited successfully",
                    "data": serializer.data,
                    "status": status.HTTP_200_OK,
                }
            )

        return Response(
            {
                "message": "Measurement details not edited",
                "data": serializer.errors,
                "status": status.HTTP_400_BAD_REQUEST,
            }
        )


class BodyMeasurementObjectDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, measurement_id):
        measurement_instance = get_object_or_404(BodyMeasurement, id=measurement_id)
        measurement_instance.delete()
        return Response(
            {
                "message": "Measurement deleted successfully",
                "status": status.HTTP_200_OK,
            }
        )
