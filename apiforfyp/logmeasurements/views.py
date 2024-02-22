from datetime import timedelta, timezone
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import BodyMeasurement
from .serializers import LogMeasurementsSerializer
from users.models import CustomUser



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

    def get(self, request, user_id, format=None):
        user = get_object_or_404(CustomUser, id=user_id)
        is_pro_member = user.is_pro_member

        if is_pro_member or user == request.user:
            if is_pro_member:
                queryset = BodyMeasurement.objects.filter(user=user)
            else:
                # Show measurements of the last 15 days
                queryset = BodyMeasurement.objects.filter(
                    user=user, created_at__gte=timezone.now() - timedelta(days=15)
                )

            serializer = LogMeasurementsSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response(
                {"detail": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN
            )
