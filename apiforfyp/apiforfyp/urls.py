"""
URL configuration for apiforfyp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views
from .views import (
    ForgotPasswordView,
    HomePageAPIView,
    PasswordCheckAPIView,
    ChangePasswordAPIView,
    TokenObtainPairView,
    TokenRefreshView,
    ChangePasswordWithOTPView,
    home,
    logouts as logot,
)

from externalfunctions.maintance_calories import UserRelatedFunction

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", view=home, name="home"),
    path(
        "logout/",
        view=logot,
        name="logout",
    ),
    path("api/resetpassword/", view=ChangePasswordWithOTPView.as_view()),
    path("api/forgotpassword/", view=ForgotPasswordView.as_view()),
    path("api/password/post/<str:user>/", view=PasswordCheckAPIView.as_view()),
    path("api/password/change/<str:user>/", view=ChangePasswordAPIView.as_view()),
    path("api/home/<str:user>/", view=HomePageAPIView.as_view()),
    path("gymbuddyadmin/", include("gymbuddyadmin.urls")),
    path("api/foods/", include("food.urls")),
    path("api/users/", include("users.urls")),
    path("api/exercise/", include("exercise.urls")),
    path("api/calories/", include("caloricintake.urls")),
    path("api/water/", include("waterintake.urls")),
    path("api/workout/", include("logworkout.urls")),
    path("api/meditation/", include("meditationintake.urls")),
    path("api/measurements/", include("logmeasurements.urls")),
    path("api/export/", include("userdata.urls")),
    # path(
    #     "api/token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"
    # ),
    path("api/token/obtain/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # path(
    #     "api/token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"
    # ),
    path(
        "api/calculate_maintance_calories/",
        view=UserRelatedFunction.calculate_maintance_calories,
    ),
    path("api/workoutroutine/", include("customroutine.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
