from rest_framework.views import APIView


class UserRelatedFunction(APIView):

    def calculate_maintance_calories(age, gender, weight, height, activity_level):
        """
        Calculate the maintance calories of a user using haris-benedict equation
        """
        bmr = 0
        if gender == "male":
            bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)

        elif gender == "female":
            bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

        if activity_level == "sedentary":
            return bmr * 1.2
        elif activity_level == "lightly_active":
            return bmr * 1.375
        elif activity_level == "moderately_active":
            return bmr * 1.55
        elif activity_level == "very_active":
            return bmr * 1.725
        elif activity_level == "super_active":
            return bmr * 1.9
        else:
            return bmr * 1.2

    def calculate_bmi(weight, height):
        """
        Calculate the BMI of a user
        """
        return weight / (height * height)
    
    def suggest_fitness_goal(bmi):
        '''
        Suggestions for fitness goals based on BMI
        '''
        
        
        
        
