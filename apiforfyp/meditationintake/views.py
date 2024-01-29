from datetime import timezone
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MeditationSerializer
from .models import Meditation

# Create your views here.


class MeditationPostAPIView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = MeditationSerializer(data=data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "status": 201,
                        "message": "Meditation added successfully",
                        "data": serializer.data,
                    }
                )
            else:
                return Response(
                    {
                        "status": 400,
                        "message": "Error Adding Meditation",
                        "data": serializer.errors,
                    }
                )
        except:
            return Response({"status": 500, "message": "Internal Server Error"})


class MeditationGetAPIView(APIView):
    def get(self, request):
        try:
            # get the user from request
            user = request.user
            current_time = timezone.now()

            # check if user is a pro member

            if user.is_pro_member:
                # if pro send all data
                queryset = Meditation.objects.all()

            else:
                # if not pro member get data from last 15 days

                fiteen_days_ago = current_time - datetime.timedelta(days=15)
                queryset = Meditation.objects.filter(date__gte=fiteen_days_ago)
            serializer = MeditationSerializer(queryset, many=True)
            return Response(
                {"status": 200, "message": "Meditation data", "data": serializer.data}
            )
        except:
            return Response({"status": 500, "message": "Internal Server Error"})
