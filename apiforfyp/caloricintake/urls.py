from django.urls import path
from caloricintake.views import CaloricIntakeView

urlpatterns = [
    path("logcalories/", view=CaloricIntakeView.as_view, name="log calories")
]
