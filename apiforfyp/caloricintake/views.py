from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from .serializers import CaloricIntakeSerializers

# Create your views here.


class CaloricIntakeView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @api_view(["POST"])
    def post(self, request):
        serializer = CaloricIntakeSerializers(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(
                serializer.data,
                {"message": "Calories logged successfully"},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"message": "Calories Logging Failed"}, status=status.HTTP_400_BAD_REQUEST
        )
