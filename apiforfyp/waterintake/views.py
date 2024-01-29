from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import WaterIntakeSerializer
from rest_framework.views import APIView
from .models import WaterIntake

# Create your views here.
# class WaterIntakeView:
#     @api_view(["POST"])
#     def log_water_intake(request):
#         serializer = WaterIntakeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response({"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)


class WaterIntakeGetView(APIView):
    def get(self, request):
        try:
            waterintake = WaterIntake.objects.all()
            serializer = WaterIntakeSerializer(waterintake, many=True)
            return Response(
                {
                    "message": "Water intake fetched successfully",
                    "data": serializer.data,
                    "status": status.HTTP_200_OK,
                }
            )
        except Exception as e:
            return Response(
                {
                    "message": "Water intake not fetched",
                    "data": str(e),
                    "status": status.HTTP_400_BAD_REQUEST,
                }
            )


class WaterIntakeView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = WaterIntakeSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "message": "Water intake set successfully",
                        "data": serializer.data,
                        "status": status.HTTP_201_CREATED,
                    }
                )
            else:
                return Response(
                    {
                        "message": "Water intake not set",
                        "data": serializer.errors,
                        "status": status.HTTP_400_BAD_REQUEST,
                    }
                )

        except Exception as e:
            return Response(
                {
                    "message": "Water intake not set",
                    "data": str(e),
                    "status": status.HTTP_400_BAD_REQUEST,
                }
            )
