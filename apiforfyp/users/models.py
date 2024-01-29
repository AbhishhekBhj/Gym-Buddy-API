from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager


# Create your models here.
class CustomUser(AbstractUser):
    id = models.AutoField(
        primary_key=True,
        blank=False,
    )
    username = models.CharField(max_length=100, blank=False, unique=True)
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

    objects = CustomUserManager()

    def __str__(self):
        return self.name
