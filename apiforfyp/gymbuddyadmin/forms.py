from django import forms
from users.models import CustomUser
from exercise.models import Exercise
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


class ExerciseForm(forms.Form):
    TARGET_BODY_PART_CHOICES = [
        (1, "Front Delts"),
        (2, "Rear Delts"),
        (3, "Quadriceps"),
        (4, "Hamstring"),
        (5, "Glutes Maximus"),
        (6, "Lower Back"),
        (7, "Lats"),
        (8, "Chest"),
        (9, "Forearms"),
        (10, "Biceps"),
        (11, "Triceps"),
        (12, "Calves"),
        (13, "Abs"),
    ]

    Type = [
        (1, "Cardiovascular"),
        (2, "Yoga"),
        (3, "Strength Training"),
        (4, "Combat Sports"),
    ]

    exercise_name = forms.CharField(max_length=100)
    exercise_details = forms.CharField(widget=forms.Textarea)
    exercise_image = forms.ImageField()
    target_body_part = forms.MultipleChoiceField(
        choices=TARGET_BODY_PART_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )
    type = forms.ChoiceField(choices=Type)
    calories_burned_per_hour = forms.IntegerField()
    added_by_user = forms.BooleanField(required=False)
    uploaded_by = forms.CharField(max_length=100, required=False)

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
