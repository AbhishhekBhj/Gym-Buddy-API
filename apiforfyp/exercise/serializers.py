from rest_framework import serializers


from .models import Exercise, TargetBodyPart


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"


class TargetBodyPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetBodyPart
        fields = "__all__"
