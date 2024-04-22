from django.shortcuts import render
from rest_framework.views import APIView
from users.models import CustomUser
from rest_framework.response import Response
from .models import FeedBack
from .serializers import FeedbackSerializer


class FeedBackView(APIView):
    @classmethod
    def post(cls, request):
        user_id = request.data.get("feedback_provided_by")

        try:
            user = CustomUser.objects.get(id=user_id)

            serializer = FeedbackSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"detail": "Feedback posted successfully"}, status=201)
            else:
                return Response(serializer.errors, status=400)

        except CustomUser.DoesNotExist:
            return Response({"detail": "User not found"}, status=404)

        except KeyError as e:
            return Response(
                {"detail": f"Missing key in request data: {str(e)}"}, status=400
            )

        except Exception as e:
            return Response({"detail": str(e)}, status=500)
