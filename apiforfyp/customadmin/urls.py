from django.urls import path
from .views import *

app_name = "customadmin"

urlpatterns = [
    path("login/", login, name="login"),
    path("admin_login/", admin_login, name="admin_login"),
    path("dashboard/", dashboard, name="dashboard"),
]
