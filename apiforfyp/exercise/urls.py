from django.urls import path
from exercise.views import ExerciseView, ExerciseTypeView, TargetBodyPartView

urlpatterns = [
    path("exercise/", ExerciseView.exercise_list, name="exercise_list"),
    path(
        "exercisebodypart/",
        TargetBodyPartView.as_view(),
        name="exercise_body_part_list",
    ),
    path(
        "exercisetype/",
        ExerciseTypeView.as_view(),
        name="exercise_type_list",
    ),
]
