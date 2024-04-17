from django import forms
from users.models import CustomUser
from exercise.models import Exercise, ExerciseType
from food.models import Food


class EditUserDetailsForm(forms.ModelForm):
    FITNESS_LEVEL_CHOICES = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
    ]

    FITNESS_GOAL_CHOICES = [
        ("weight_loss", "Weight Loss"),
        ("muscle_gain", "Muscle Gain"),
        ("maintenance", "Maintenance"),
    ]

    fitness_level = forms.ChoiceField(choices=FITNESS_LEVEL_CHOICES)
    fitness_goal = forms.ChoiceField(choices=FITNESS_GOAL_CHOICES)

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "name",
            "email",
            "age",
            "height",
            "weight",
            "fitness_level",
            "fitness_goal",
            "profile_picture",
            "is_verified",
            "is_pro_member",
        ]


class AddNewUserForm(forms.ModelForm):
    FITNESS_LEVEL_CHOICES = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
    ]

    FITNESS_GOAL_CHOICES = [
        ("weight_loss", "Weight Loss"),
        ("muscle_gain", "Muscle Gain"),
        ("maintenance", "Maintenance"),
    ]

    fitness_level = forms.ChoiceField(choices=FITNESS_LEVEL_CHOICES)
    fitness_goal = forms.ChoiceField(choices=FITNESS_GOAL_CHOICES)

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "password",
            "name",
            "email",
            "age",
            "height",
            "weight",
            "fitness_level",
            "fitness_goal",
            "profile_picture",
            "is_verified",
            "is_pro_member",
        ]


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = [
            "exercise_name",
            "exercise_details",
            "exercise_image",
            "target_body_part",
            "type",
            "calories_burned_per_hour",
            "added_by_user",
            "uploaded_by",
        ]
        widgets = {
            "type": forms.Select(attrs={"class": "form-control"}),
            "exercise_details": forms.Textarea(attrs={"rows": 10, "cols": 15}),
            "target_body_part": forms.CheckboxSelectMultiple(),
        }


class AddNewExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = [
            "exercise_name",
            "exercise_details",
            "exercise_image",
            "target_body_part",
            "type",
            "calories_burned_per_hour",
            "added_by_user",
            "uploaded_by",
        ]
        widgets = {
            "type": forms.RadioSelect(),
            "exercise_details": forms.Textarea(attrs={"rows": 10, "cols": 15}),
            "target_body_part": forms.CheckboxSelectMultiple(),
        }


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = [
            "food_name",
            "food_image",
            "food_description",
            "food_serving_size",
            "food_protein_per_servings",
            "food_calories_per_serving",
            "food_carbs_per_serving",
            "food_fat_per_serving",
            "added_by_user",
            "uploaded_by",
        ]


class EditFoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = [
            "food_name",
            "food_image",
            "food_description",
            "food_serving_size",
            "food_protein_per_servings",
            "food_calories_per_serving",
            "food_carbs_per_serving",
            "food_fat_per_serving",
            "added_by_user",
            "uploaded_by",
        ]
