from django.urls import path
from .views import MeditationPostAPIView, MeditationGetAPIView


urlpatterns = [
    path("post/", MeditationPostAPIView.as_view()),
    path("get/", MeditationGetAPIView.as_view()),
]
