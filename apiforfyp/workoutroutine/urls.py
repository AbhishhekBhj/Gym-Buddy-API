from django.urls import path
from .views import *

urlpatterns = [
    path("addcustomroutine/", CustomRoutineCreateView.as_view()),
    path("getcustomroutine/", CustomRoutineGetView.as_view()),
]
