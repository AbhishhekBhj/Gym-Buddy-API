from django.urls import path


from .views import RemindersSetAPIView, RemindersGetAPIView


urlpatterns = [
    path("set/", RemindersSetAPIView.as_view(), name="set_reminder"),
    path("get/", RemindersGetAPIView.as_view(), name="get_reminders"),
]
