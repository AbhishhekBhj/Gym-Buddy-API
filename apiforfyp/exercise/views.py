from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import (
    ExerciseSerializer,
    ExerciseTypeSerializer,
    TargetBodyPartSerializer,
)
from .models import Exercise, TargetBodyPart, ExerciseType
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from users.models import CustomUser


# Create your views here.


class ExerciseView(APIView):
    def get(request, format=None):
        exercise = Exercise.objects.all()
        serializer = ExerciseSerializer(exercise, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # remove in production
    @api_view(["POST"])
    def post(request):
        serializer = ExerciseSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @api_view(["GET", "PUT"])
    # def exercise_body_part_list(request):
    #     if request.method == "GET":
    #         target_body_part = TargetBodyPart.objects.all()
    #         serializer = TargetBodyPartSerializer(target_body_part, many=True)
    #         return Response(serializer.data, status=status.HTTP_200_OK)

    #     if request.method == "POST":
    #         target_body_part = TargetBodyPart.objects.all()
    #         serializer = TargetBodyPartSerializer(target_body_part, many=True)
    #         return Response(serializer.data, status=status.HTTP_200_OK)


class CustomExerciseView(APIView):
    def post(self, request):
        try:
            serializer = ExerciseSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "status": 200,
                        "message": "Exercise added successfully",
                        "data": serializer.data,
                    }
                )

            else:
                return Response(
                    {
                        "status": 400,
                        "message": "Exercise addition failed",
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


class TargetBodyPartView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = TargetBodyPartSerializer(data=data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "status": 200,
                        "message": "Target Body Part added successfully",
                        "data": serializer.data,
                    }
                )
            return Response(
                {
                    "status": 400,
                    "message": "Target Body Part addition failed",
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

    def get(self, request):
        try:
            target_body_part = TargetBodyPart.objects.all()
            serializer = TargetBodyPartSerializer(target_body_part, many=True)
            return Response(
                {
                    "status": 200,
                    "message": "Target Body Part retrieved successfully",
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


class ExerciseTypeView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = ExerciseTypeSerializer(data=data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "status": 200,
                        "message": "Exercise Type added successfully",
                        "data": serializer.data,
                    }
                )
            return Response(
                {
                    "status": 400,
                    "message": "Exercise Type addition failed",
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

    def get(self, request):
        try:
            exercise_type = ExerciseType.objects.all()
            serializer = ExerciseTypeSerializer(exercise_type, many=True)
            return Response(
                {
                    "status": 200,
                    "message": "Exercise Type retrieved successfully",
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


class UploadCustomExercise(APIView):
    def post(self, request, user):
        try:
            user_instance = CustomUser.objects.get(username=user)

            exercise_data = request.data
            exercise_data["added_by_user"] = True
            
            
            exercise_data["uploaded_by"] = (
                user_instance.id
            )  

            serializer = ExerciseSerializer(data=exercise_data)

            if serializer.is_valid():
                if not user_instance.is_pro_member:
                    if user_instance.number_of_customexercises >= 5:
                        return Response(
                            {
                                "status": 400,
                                "message": "Free users can only upload 5 custom exercises",
                            }
                        )

                user_instance.number_of_customexercises += 1
                user_instance.save()
                serializer.save()
                return Response(
                    {
                        "status": 200,
                        "message": "Exercise added successfully",
                        "data": serializer.data,
                        "uploaded_by": user_instance.username,
                    }
                )
            else:
                return Response(
                    {
                        "status": 400,
                        "message": "Exercise addition failed",
                        "data": serializer.errors,
                    }
                )

        except CustomUser.DoesNotExist:
            return Response(
                {
                    "status": 404,
                    "message": "User not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {
                    "status": 500,
                    "message": "Internal Server Error",
                    "data": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
