from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import CustomMeal
from .serializers import CustomMealSerializer
from .models import CustomUser

# Create your views here.


class CustomMealView(APIView):
    def get(self, request, user):
        try:
            # get who is making the request
            user_instance = CustomUser.objects.get(username=user)
            # get custom meals made by the user
            meal = CustomMeal.objects.get(uploaded_by=user_instance)

            serializer = CustomMealSerializer(meal, many=True)
            return Response(
                {
                    "status": 200,
                    "message": "Meals fetched successfully",
                    "data": serializer.data,
                }
            )
            # if user does not exist
        except CustomUser.DoesNotExist:
            return Response(
                {
                    "status": status.HTTP_404_NOT_FOUND,
                    "message": "User not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        # if no meals are found
        except CustomMeal.DoesNotExist:
            return Response(
                {
                    "status": status.HTTP_404_NOT_FOUND,
                    "message": "No meals found for the user",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        except Exception as e:
            return Response(
                {
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "Meals not fetched",
                    "data": str(e),
                }
            )


class CustomMealPostView(APIView):
    def post(self, request):
        try:
            serializer = CustomMealSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "status": 200,
                        "message": "Meal added successfully",
                        "data": serializer.data,
                    }
                )
            else:
                return Response(
                    {
                        "status": 400,
                        "message": "Meal not added",
                        "data": serializer.errors,
                    }
                )

        except Exception as e:
            return Response(
                {
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "Meal not added",
                    "data": str(e),
                }
            )
