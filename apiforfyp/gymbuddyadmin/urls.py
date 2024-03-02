from django.urls import path
from .views import (
    login,
    adminlogin,
    userpage,
    exercises,
    food,
    delete_item,
    edit_food,
    edit_user,
    view_profile,
    dashboard,
    add_new_user,
    register_new_user,
    alter_user_details,
)

urlpatterns = [
    path("login/", login, name="custom_login"),
    path("performlogin/", adminlogin, name="performlogin"),
    path("users/", userpage, name="users"),
    path("exercises/", exercises, name="exercises"),
    path("food/", food, name="food"),
    path("delete_item/<int:item_id>/", delete_item, name="delete_item"),
    path("edit_item/<int:item_id>/", edit_food, name="edit_food"),
    path("edituser/<int:user_id>/", edit_user, name="edit_user"),
    path("viewprofile/<int:user_id>", view_profile, name="view_profile"),
    path("dashboard/", dashboard, name="dashboard"),
    path("adduser/", add_new_user, name="add_new_user"),
    path("registeruser/", register_new_user, name="register_new_user"),
    path("alteruser/<str:username>/", alter_user_details, name="alter_user_details"),
]
