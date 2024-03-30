from rest_framework import serializers
from .models import Workout
from exercise.models import Exercise, TargetBodyPart, ExerciseType


class TargetBodyPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetBodyPart
        fields = ["id", "name"]


class ExerciseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseType
        fields = ["id", "name"]


class ExerciseSerializer(serializers.ModelSerializer):
    target_body_part = TargetBodyPartSerializer(many=True, read_only=True)
    type = ExerciseTypeSerializer(read_only=True)

    class Meta:
        model = Exercise
        fields = "__all__"


class WorkoutSerializer(serializers.ModelSerializer):

    exercise = ExerciseSerializer(source="exercise_id", read_only=True)

    class Meta:
        model = Workout
        fields = "__all__"
