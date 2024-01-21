
from django.urls import path,include
from food.views import FoodView
urlpatterns = [
   path('getfood/',view=FoodView.food_list,name='food_list'),
   path('editfood/<int:pk>/',view=FoodView.food_list_edit,name='food_list_edit'),
   path('get_food_details/<str:food_name>/',view=FoodView.get_food_details,name='get_food_details')]
