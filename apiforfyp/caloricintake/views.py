import datetime
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from .serializers import CaloricIntakeSerializers
from django.utils import timezone
from .models import CaloricIntake

# Create your views here.


class CaloricIntakeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = CaloricIntakeSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "data": serializer.data,
                        "status": 201,
                        "message": "Caloric Intake Object Created",
                    }
                )

            else:
                return Response(
                    {
                        "message": "Caloric Intake Object Not Created",
                        "status": 400,
                        "data": serializer.errors,
                    }
                )
        except Exception as e:
            return Response(
                {
                    "status": 500,
                    "message": "Internal Server Error",
                    "data": str(e),
                }
            )


class CaloricIntakeGetView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, user):

        try:

            # get user from request
            user = request.user
            current_time = timezone.now()

            # check whether pro member

            if user.is_pro_member:

                # send all time data
                queryset = CaloricIntake.objects.filter(username_id=user).all()

            else:
                # if not pro member send last 15 day data
                fifteen_days_ago = current_time - datetime.timedelta(days=15)
                queryset = CaloricIntake.objects.filter(
                    created_at__gte=fifteen_days_ago
                )

            serializer = CaloricIntakeSerializers(queryset, many=True)

            return Response(
                {
                    "status": 200,
                    "message": "Caloric Intake data",
                    "data": serializer.data,
                }
            )

        except Exception as e:
            return Response(
                {
                    "status": 500,
                    "message": "Internal Server Error",
                    "data": str(e),
                }
            )
