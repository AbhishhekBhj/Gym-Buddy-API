from rest_framework import generics
from .models import MealPlan, Food
from .serializers import MealPlanSerializer, FoodSerializer
from rest_framework.response import Response




class MealPlanListByUserAPIView(generics.ListAPIView):
    serializer_class = MealPlanSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return MealPlan.objects.filter(user_id=user_id)

class MealPlanListCreateAPIView(generics.ListCreateAPIView):
    queryset = MealPlan.objects.all()
    serializer_class = MealPlanSerializer


class MealPlanRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MealPlan.objects.all()
    serializer_class = MealPlanSerializer


class FoodListCreateAPIView(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    
    
    
class UpdateMealItemAPIView(generics.UpdateAPIView):
    queryset = MealPlan.objects.all()
    serializer_class = MealPlanSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()  
        food_id_to_update = request.data.get('food_id')  
        new_food_data = request.data.get('new_food_data')  

        for food_item in instance.foods.all():
            if food_item.id == food_id_to_update:
                for attr, value in new_food_data.items():
                    setattr(food_item, attr, value)
                food_item.save()
                break
        
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
