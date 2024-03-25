import matplotlib.pyplot as plt
import numpy as np
from django.shortcuts import render
from caloricintake.models import CaloricIntake

def generate_bar_chart(request):
    # Retrieve data from Django model (CaloricIntake in this example)
    caloric_intakes = CaloricIntake.objects.all()

    # Process data
    usernames = [caloric_intake.username for caloric_intake in caloric_intakes]
    calories_consumed = [caloric_intake.calories_consumed for caloric_intake in caloric_intakes]

    # Create bar chart
    plt.bar(usernames, calories_consumed)
    plt.xlabel('Usernames')
    plt.ylabel('Calories Consumed')
    plt.title('Calories Consumed by User')

    chart_image_path = 'chart.png'
    plt.savefig(chart_image_path)

    plt.close()

    return render(request, 'caloric_intake_graph.html', {'chart_image_path': chart_image_path})
