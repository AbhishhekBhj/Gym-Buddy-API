from django.urls import path
from caloricintake.views import CaloricIntakeView, CaloricIntakeGetView

urlpatterns = [
    path("logcalories/", view=CaloricIntakeView.as_view(), name="log calories"),
    path(
        "get_calories/<str:user>/", view=CaloricIntakeGetView.as_view(), name="calories"
    ),
]
