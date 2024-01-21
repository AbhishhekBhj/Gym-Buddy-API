from django.contrib import admin
from .models import Food
from users.models import CustomUser
from exercise.models import Exercise, TargetBodyPart

# Register your models here.

admin.site.register(Food)
admin.site.register(CustomUser)
admin.site.register(Exercise)
admin.site.register(TargetBodyPart)
