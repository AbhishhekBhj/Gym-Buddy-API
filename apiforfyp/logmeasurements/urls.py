from django.urls import path
from .views import *

urlpatterns = [
    path("addmeasurement/", BodyMeasurementListCreateView.as_view()),
    path("addmeasurementpro/", BodyMeasurementListCreateViewPro.as_view()),
    path("getmeasurement/<int:user_id>/", BodyMeasurementDetailView.as_view()),
]
