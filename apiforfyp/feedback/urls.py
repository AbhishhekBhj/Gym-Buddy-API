from django.urls import path
from .views import FeedBackView

urlpatterns = [
    path("postfeedback/", FeedBackView.as_view(), name="postfeedback"),
]
