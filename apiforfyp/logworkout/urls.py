from django.urls import path

from .views import WorkoutView, WorkoutGetView,WorkoutObjectDeleteView


urlpatterns = [
    path("logworkout/", WorkoutView.as_view(), name="logworkout"),
    path("getworkout/", WorkoutGetView.as_view(), name="getworkout"),
    path("deleteworkout/",WorkoutObjectDeleteView.as_view(),name="delete_workout"),
    
]
