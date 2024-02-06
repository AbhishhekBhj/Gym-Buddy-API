from django.urls import path
from .views import *

urlpatterns = [
    path("addmeasurement/<int:id>/", BodyMeasurementListCreateView.as_view()),
    path("getmeasurement/<int:user_id>/", BodyMeasurementDetailView.as_view()),
]