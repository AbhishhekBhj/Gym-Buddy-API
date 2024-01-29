from django.urls import path
from waterintake.views import WaterIntakeView, WaterIntakeGetView

urlpatterns = [
    path("log/", WaterIntakeView.as_view(), name="log_water_intake"),
    path("get/", WaterIntakeGetView.as_view(), name="get_water_intake"),
]
