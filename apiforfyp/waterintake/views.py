from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import WaterIntakeSerializer


# Create your views here.
class WaterIntakeView:
    @api_view(["POST"])
    def log_water_intake(request):
        serializer = WaterIntakeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)
