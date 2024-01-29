from django.contrib import admin
from .models import Food
from users.models import CustomUser
from exercise.models import *
from logworkout.models import *
from waterintake.models import *
from meditationintake.models import *
from reminders.models import *

# Register your models here.

admin.site.register(Food)
admin.site.register(CustomUser)
admin.site.register(Exercise)
admin.site.register(TargetBodyPart)
admin.site.register(ExerciseType)
admin.site.register(Workout)
admin.site.register(Meditation)
admin.site.register(WaterIntake)
admin.site.register(Reminder)
