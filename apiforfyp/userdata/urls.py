from django.urls import path
from .views import *

urlpatterns = [
    path("userdata/<str:user>/", view=GetUsersProfileData.as_view(), name="userdata"),
    path(
        "customexercises/<str:user>/",
        view=GetCustomExercises.as_view(),
        name="customexercises",
    ),
    path("customfoods/<str:user>/", view=GetCustomFood.as_view(), name="customfoods"),
    path(
        "workout/<str:user>/",
        view=GetWorkoutData.as_view(),
        name="workouts",
    ),
    path(
        "caloricintake/<str:user>/",
        view=GetCaloricIntakeData.as_view(),
        name="workouts",
    ),
    path(
        "waterintake/<str:user>/",
        view=GetWaterIntake.as_view(),
        name="waterintake",
    ),
]
