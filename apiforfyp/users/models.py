from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager
from django.utils import timezone
from dateutil.relativedelta import relativedelta


# Create your models here.
class CustomUser(AbstractUser):
    id = models.AutoField(
        primary_key=True,
        blank=False,
    )
    username = models.CharField(max_length=100, blank=False, unique=True)
    height = models.FloatField(default=0, blank=False)
    weight = models.FloatField(default=0, blank=False)
    gender = models.CharField(max_length=100, blank=False, default="Male")
    name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(default=0, blank=False)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False)
    fitness_level = models.CharField(max_length=100, blank=False)
    fitness_goal = models.CharField(max_length=100, blank=False)
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", blank=True, null=True
    )
    last_login = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, blank=True, null=True)
    is_pro_member = models.BooleanField(default=False)

    number_of_custom_routines = models.IntegerField(default=0)
    number_of_customexercises = models.IntegerField(default=0)
    number_of_customfood = models.IntegerField(default=0)
    number_of_custommeals = models.IntegerField(default=0)

    bmi = models.FloatField(default=0)
    recommended_calories = models.FloatField(default=0)

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class OTP(models.Model):
    email = models.EmailField()
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)


class Subscription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subscription_type = models.CharField(
        max_length=20,
        choices=[
            ("1", "Monthly"),
            ("2", "6 Monthly"),
            ("3", "Yearly"),
        ],
    )
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()

    @property
    def is_pro_member(self):
        return self.end_date is not None and self.end_date > timezone.now()

    def activate_subscription(self):
        print(f"Before activation: End Date - {self.end_date}")
        if self.subscription_type == "1":
            if self.end_date:
                self.end_date += relativedelta(months=1)  # Extend by one month
            else:
                self.end_date = timezone.now() + relativedelta(
                    months=1
                )  # Set initial end date to one month from now
        elif self.subscription_type == "2":
            if self.end_date:
                self.end_date += relativedelta(months=6)  # Extend by six months
            else:
                self.end_date = timezone.now() + relativedelta(months=6)
        elif self.subscription_type == "3":
            if self.end_date:
                self.end_date += relativedelta(years=1)  # Extend by one year
            else:
                self.end_date = timezone.now() + relativedelta(years=1)

        print(f"After activation: End Date - {self.end_date}")

        self.save()
        return f"Subscription extended till {self.end_date} by {self.subscription_type} for user {self.user.username}"

    def __str__(self):
        return self.user.username
