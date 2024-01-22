from django.urls import path
from waterintake.views import WaterIntakeView

urlpatterns = [path("log/", WaterIntakeView.log_water_intake, name="log_water_intake")]
