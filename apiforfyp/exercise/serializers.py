from rest_framework import serializers


from .models import Exercise, TargetBodyPart, ExerciseType


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"


class TargetBodyPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetBodyPart
        fields = ("id", "name")


class ExerciseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseType
        fields = "__all__"
