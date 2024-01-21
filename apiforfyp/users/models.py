from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(default=0, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    password = models.CharField(max_length=100, blank=False)
    fitness_level = models.CharField(max_length=100, blank=False)
    fitness_goal = models.CharField(max_length=100, blank=False)
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", blank=True, null=True
    )
    last_login = models.DateTimeField(auto_now=True, blank=True, null=True)
