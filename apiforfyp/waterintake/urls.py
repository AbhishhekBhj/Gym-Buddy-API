from django.urls import path
from waterintake.views import WaterIntakeView, WaterIntakeGetView,EditWaterIntakeObjectDetails,DeleteWaterIntakeObject

urlpatterns = [
    path("log/", WaterIntakeView.as_view(), name="log_water_intake"),
    path("get/<str:user>/", WaterIntakeGetView.as_view(), name="get_water_intake"),
    path("edit/<int:waterintake_id>/", EditWaterIntakeObjectDetails.as_view(), name="edit_water_intake"),
    path("delete/", DeleteWaterIntakeObject.as_view(), name="delete_water_intake"),
]
