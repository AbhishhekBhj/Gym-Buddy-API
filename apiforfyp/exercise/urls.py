from django.urls import path
from exercise.views import (
    ExerciseView,
    ExerciseTypeView,
    TargetBodyPartView,
    UploadCustomExercise,
)

urlpatterns = [
    path("exercise/", ExerciseView.get, name="exercise_list"),
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
    path("post/", ExerciseView.post, name="exercise_post"),
    path(
        "custompost/<str:user>/",
        UploadCustomExercise.as_view(),
        name="custom_exercise_post",
    ),
]
