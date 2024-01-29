from django.urls import path
from .views import  UserRegistrationView,LoginAPIView,VerifyOTPAPI,ResendOTPView, LoginAPIView


urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    # path("login/", LoginView, name="login"),
    path("verify-otp/", VerifyOTPAPI.as_view(), name="verify-otp"),
    path("resend-otp/", ResendOTPView.as_view(), name="resend-otp"),
    path("login/", LoginAPIView.as_view(), name="login"),
]
