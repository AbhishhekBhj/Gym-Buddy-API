from django import forms
from users.models import CustomUser


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
            # "email",
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
