from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from food.models import Food
from food.serializers import FoodSerializer
from users.models import CustomUser
from exercise.models import Exercise
from exercise.serializers import ExerciseSerializer
from users.serializers import UserSerializer
from logworkout.models import Workout
from logworkout.serializer import WorkoutSerializer
from caloricintake.models import CaloricIntake
from caloricintake.serializers import CaloricIntakeSerializers
from waterintake.models import WaterIntake
from waterintake.serializers import WaterIntakeSerializer


class GetUsersProfileData(APIView):
    def get(self, request, user):
        try:
            user = CustomUser.objects.get(username=user)
            serializer = UserSerializer(user)
            return Response(
                {
                    "status": 200,
                    "message": "User data fetched successfully",
                    "data": serializer.data,
                }
            )

        except CustomUser.DoesNotExist:
            return Response(
                {
                    "status": status.HTTP_404_NOT_FOUND,
                    "message": "User not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        except Exception as e:
            return Response(
                {
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "User data not fetched",
                    "data": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class GetCustomExercises(APIView):
    def get(self, request, user):
        try:
            user = CustomUser.objects.get(username=user)
            exercises = Exercise.objects.filter(uploaded_by=user.id)
            serializer = ExerciseSerializer(exercises, many=True)

            if not exercises:
                return Response(
                    {
                        "status": status.HTTP_404_NOT_FOUND,
                        "message": "No custom exercises of this user found",
                    }
                )
            return Response(
                {
                    "status": 200,
                    "message": "Exercises fetched successfully",
                    "data": serializer.data,
                }
            )

        except CustomUser.DoesNotExist:
            return Response(
                {
                    "status": status.HTTP_404_NOT_FOUND,
                    "message": "User not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        except Exception as e:
            return Response(
                {
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "Exercises not fetched",
                    "data": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class GetCustomFood(APIView):
    def get(self, request, user):
        try:
            user = CustomUser.objects.get(username=user)
            food = Food.objects.filter(uploaded_by=user.id)
            serializer = FoodSerializer(food, many=True)

            if not food:
                return Response(
                    {
                        "status": status.HTTP_404_NOT_FOUND,
                        "message": "No custom food of this user found",
                    }
                )
            return Response(
                {
                    "status": 200,
                    "message": "Food fetched successfully",
                    "data": serializer.data,
                }
            )

        except CustomUser.DoesNotExist:
            return Response(
                {
                    "status": status.HTTP_404_NOT_FOUND,
                    "message": "User not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        except Exception as e:
            return Response(
                {
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "Food not fetched",
                    "data": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class GetWorkoutData(APIView):
    def get(self, request, user):
        try:
            user = CustomUser.objects.get(username=user)
            workout = Workout.objects.filter()
            serializer = WorkoutSerializer(workout, many=True)

            if not workout:
                return Response(
                    {
                        "status": status.HTTP_404_NOT_FOUND,
                        "message": "No workout data found",
                    }
                )
            return Response(
                {
                    "status": 200,
                    "message": "Workout data fetched successfully",
                    "data": serializer.data,
                }
            )

        except CustomUser.DoesNotExist:
            return Response(
                {
                    "status": status.HTTP_404_NOT_FOUND,
                    "message": "User not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        except Exception as e:
            return Response(
                {
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "Workout data not fetched",
                    "data": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class GetCaloricIntakeData(APIView):
    def get(self, request, user):
        try:
            user = CustomUser.objects.get(username=user)
            caloricintake = CaloricIntake.objects.filter(username=user.id)
            serializer = CaloricIntakeSerializers(caloricintake, many=True)

            if not caloricintake:
                return Response(
                    {
                        "status": status.HTTP_404_NOT_FOUND,
                        "message": "No caloric intake data found",
                    }
                )
            return Response(
                {
                    "status": 200,
                    "message": "Caloric intake data fetched successfully",
                    "data": serializer.data,
                }
            )

        except CustomUser.DoesNotExist:
            return Response(
                {
                    "status": status.HTTP_404_NOT_FOUND,
                    "message": "User not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        except Exception as e:
            return Response(
                {
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "Caloric intake data not fetched",
                    "data": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class GetWaterIntake(APIView):
    def get(self, request, user):
        try:
            user = CustomUser.objects.get(username=user)
            waterintake = WaterIntake.objects.filter(user_id=user.id)
            serializer = WaterIntakeSerializer(waterintake, many=True)

            if not waterintake:
                return Response(
                    {
                        "status": status.HTTP_404_NOT_FOUND,
                        "message": "No water intake data found",
                    }
                )
            return Response(
                {
                    "status": 200,
                    "message": "Water intake data fetched successfully",
                    "data": serializer.data,
                }
            )

        except CustomUser.DoesNotExist:
            return Response(
                {
                    "status": status.HTTP_404_NOT_FOUND,
                    "message": "User not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        except Exception as e:
            return Response(
                {
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "Water intake data not fetched",
                    "data": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
