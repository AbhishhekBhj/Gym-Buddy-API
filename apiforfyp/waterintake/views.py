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
    """
    API view to retrieve all water intake records.

    Methods:
    - get: Retrieves all water intake records and returns a response with the data.

    Returns:
    - Response: A response object containing the fetched water intake records.
    """
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
    """
    API view for setting water intake.
    """

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
            
            
class EditWaterIntakeObjectDetails(APIView):
    """
    API view for editing the details of a water intake object.
    """

    def patch(self, request, intake_id):
        try:
            # get object with id
            water_instance = WaterIntake.objects.get(id=intake_id)
            data = request.data

            serializer = WaterIntakeSerializer(water_instance, data=data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "message": "Water Intake Object Updated",
                        "data": serializer.data,
                        "status": status.HTTP_200_OK,
                    }
                )

            else:
                return Response(
                    {
                        "message": "Water Intake Object Not Updated",
                        "data": serializer.errors,
                        "status": status.HTTP_400_BAD_REQUEST,
                    }
                )

        # if water intake not found
        except WaterIntake.DoesNotExist:
            return Response(
                {
                    "message": "Water Intake Object Not Found",
                    "status": status.HTTP_404_NOT_FOUND,
                }
            )
        except Exception as e:
            return Response(
                {
                    "message": "Internal Server Error",
                    "data": str(e),
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                }
            )
            
            
class DeleteWaterIntakeObject(APIView):
    """
    API view for deleting a water intake object.
    """

    def delete(self, request, intake_id):
        try:
            # get object with id
            water_instance = WaterIntake.objects.get(id=intake_id)
            water_instance.delete()
            return Response(
                {
                    "message": "Water Intake Object Deleted",
                    "status": status.HTTP_200_OK,
                }
            )

        # if water intake not found
        except WaterIntake.DoesNotExist:
            return Response(
                {
                    "message": "Water Intake Object Not Found",
                    "status": status.HTTP_404_NOT_FOUND,
                }
            )
        except Exception as e:
            return Response(
                {
                    "message": "Internal Server Error",
                    "data": str(e),
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                }
            )
