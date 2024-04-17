from django.urls import path
from .views import (
    UserRegistrationView,
    LoginAPIView,
    VerifyOTPAPI,
    ResendOTPView,
    LoginAPIView,
    UploadProfilePicture,
    EditUserDetails,
    UserDeleteAccountView,
    MakeMeProUser,
    GetUserData
)


urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    # path("login/", LoginView, name="login"),
    path("verify-otp/", VerifyOTPAPI.as_view(), name="verify-otp"),
    path("resend-otp/", ResendOTPView.as_view(), name="resend-otp"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path(
        "uploadprofilephoto/",
        view=UploadProfilePicture.as_view(),
        name="uploadprofile",
    ),
    path("editprofile/", view=EditUserDetails.as_view(), name="editprofile"),
    path("delete/<int:user>/", view=UserDeleteAccountView.as_view(), name="deleteuser"),
    path("makemeprouser/", view=MakeMeProUser.as_view(), name="makemeprouser"),
    path("getuserdata/", view=GetUserData.as_view(), name="getuserdata"),
]
