from django.urls import path

from meals.views import CustomMealView,CustomMealPostView


urlpatterns = [
    path("meals/<str:user>/", CustomMealView.as_view(), name="meals_list"),
    path("meals/post/", CustomMealPostView.as_view(), name="meals_post"),
]
