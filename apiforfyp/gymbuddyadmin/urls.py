from django.urls import path
from .views import login, adminlogin, userpage, exercises, food, delete_item, edit_item

urlpatterns = [
    path("login/", login, name="custom_login"),
    path("performlogin/", adminlogin, name="performlogin"),
    path("users/", userpage, name="users"),
    path("exercises/", exercises, name="exercises"),
    path("food/", food, name="food"),
    path("delete_item/<int:item_id>/", delete_item, name="delete_item"),
    path("edit_item/<int:item_id>/", edit_item, name="edit_item")
]
