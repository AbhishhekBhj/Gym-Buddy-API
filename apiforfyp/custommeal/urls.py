from django.urls import path
from .views import (
    MealPlanListCreateAPIView,
    MealPlanRetrieveUpdateDestroyAPIView,
    FoodListCreateAPIView,
    FoodRetrieveUpdateDestroyAPIView,
    MealPlanListByUserAPIView,
    UpdateMealItemAPIView,
)

urlpatterns = [
    path("meal-plans/", MealPlanListCreateAPIView.as_view(), name="meal-plan-list"),
    path(
        "meal-plans/<int:pk>/",
        MealPlanRetrieveUpdateDestroyAPIView.as_view(),
        name="meal-plan-detail",
    ),
    path("food-items/", FoodListCreateAPIView.as_view(), name="food-item-list"),
    path(
        "food-items/<int:pk>/",
        FoodRetrieveUpdateDestroyAPIView.as_view(),
        name="food-item-detail",
    ),
    path(
        "meal-plans/user/<int:user_id>/",
        MealPlanListByUserAPIView.as_view(),
        name="meal-plans-by-user",
    ),
    path(
        "meal-plans/<int:pk>/update-food/",
        UpdateMealItemAPIView.as_view(),
        name="update_meal_item",
    ),
]
