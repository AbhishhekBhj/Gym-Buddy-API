from datetime import timedelta, timezone
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import BodyMeasurement
from .serializers import LogMeasurementsSerializer
from users.models import CustomUser


class BodyMeasurementListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = self.request.user
        is_pro_member = CustomUser.objects.get(user=user).is_pro_member
        if is_pro_member:
            queryset = BodyMeasurement.objects.filter(user=user)
        else:
            # Show measurements of the last 15 days
            queryset = BodyMeasurement.objects.filter(
                user=user, created_at__gte=timezone.now() - timedelta(days=15)
            )

        serializer = LogMeasurementsSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LogMeasurementsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
