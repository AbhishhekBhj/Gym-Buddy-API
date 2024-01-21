from django.urls import path
from exercise.views import ExerciseView

urlpatterns = [
    path("getexercise/", ExerciseView.exercise_list, name="exercise_list"),
    path(
        "getexercisebodypart/",
        ExerciseView.exercise_body_part_list,
        name="exercise_body_part_list",
    ),
]
