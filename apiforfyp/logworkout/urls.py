from django.urls import path

from .views import WorkoutView


urlpatterns = [
    path("logworkout/", WorkoutView.as_view(), name="logworkout"),
]
