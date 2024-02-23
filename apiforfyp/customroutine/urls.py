from django.urls import path
from .views import GetRoutine, PostRoutine

urlpatterns = [
    path("get/", view=GetRoutine.as_view()),
    path("post/", view=PostRoutine.as_view()),
]
