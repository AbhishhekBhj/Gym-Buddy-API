from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ExerciseSerializer, TargetBodyPartSerializer
from .models import Exercise, TargetBodyPart

# Create your views here.


class ExerciseView:
    @api_view(["GET", "POST"])
    def exercise_list(request, format=None):
        if request.method == "GET":
            exercise = Exercise.objects.all()
            serializer = ExerciseSerializer(exercise, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == "POST":
            serializer = ExerciseSerializer(data=request.data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @api_view(["GET", "PUT"])
    def exercise_body_part_list(request):
        if request.method == "GET":
            target_body_part = TargetBodyPart.objects.all()
            serializer = TargetBodyPartSerializer(target_body_part, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if request.method == "POST":
            target_body_part = TargetBodyPart.objects.all()
            serializer = TargetBodyPartSerializer(target_body_part, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
