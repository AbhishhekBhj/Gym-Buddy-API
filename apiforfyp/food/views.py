from django.shortcuts import redirect, render
from .serializers import FoodSerializer
from .models import Food
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import CustomUser

from rest_framework.views import APIView

# Create your views here.


class FoodView:
    # admin functions
    @api_view(["GET", "POST"])
    def food_list(request, format=None):
        if request.method == "GET":
            food = Food.objects.all()
            serializer = FoodSerializer(food, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == "POST":
            serializer = FoodSerializer(data=request.data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(["PUT", "DELETE", "PATCH"])
    def food_list_edit(request, pk, Format=None):
        try:
            food = Food.objects.get(pk=pk)
        except Food.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == "PUT":
            serializer = FoodSerializer(food, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == "DELETE":
            food.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        elif request.method == "PATCH":
            serializer = FoodSerializer(food, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # client function

    @api_view(["GET"])
    def get_food_details(request, food_name):
        try:
            food_details = Food.objects.filter(food_name__icontains=food_name)

            serializer = FoodSerializer(food_details, many=True)

            if len(serializer.data) == 0:
                return Response(
                    {
                        "message": "No food found with the given name",
                        "status": status.HTTP_404_NOT_FOUND,
                    }
                )

            return Response(
                {"status": 200, "data": serializer.data, "message": "success"}
            )

        except Food.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class AddCustomFoodItem(APIView):
    def post(self, request, user):
        try:
            user_instance = CustomUser.objects.get(username=user)
            food_data = request.data
            food_data["added_by_user"] = True
            food_data["uploaded_by"] = user_instance.id

            serializer = FoodSerializer(data=food_data)

            if serializer.is_valid():
                if not user_instance.is_pro_member:
                    if user_instance.number_of_customfoods >= 2:
                        return Response(
                            {
                                "status": 400,
                                "message": "Free users can only upload 2 custom foods",
                            }
                        )

                user_instance.number_of_customfoods += 1
                user_instance.save()
                serializer.save()
                return Response(
                    {
                        "status": 200,
                        "message": "Food added successfully",
                        "data": serializer.data,
                        "uploaded_by": user_instance.username,
                    }
                )
            else:
                return Response(
                    {
                        "status": 400,
                        "message": "Food addition failed",
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



