from django.urls import path
from .views import *

urlpatterns = [
    path("addmeasurement/", BodyMeasurementListCreateView.as_view()),
    path("addmeasurementpro/", BodyMeasurementListCreateViewPro.as_view()),
    path("getmeasurement/", BodyMeasurementDetailView.as_view()),
    path(
        "editmeasurement/<int:measurement_id>/", BodyMeasurementObjectEditView.as_view()
    ),
    path(
        "deletemeasurement/<int:measurement_id>/",
        BodyMeasurementObjectDeleteView.as_view(),
    ),
]
