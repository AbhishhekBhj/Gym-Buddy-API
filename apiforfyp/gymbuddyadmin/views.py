from django.shortcuts import render, get_object_or_404

from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import HttpResponse
from users.models import CustomUser, Subscription
from exercise.models import Exercise, TargetBodyPart, ExerciseType
from food.models import Food
from food.serializers import FoodSerializer
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from feedback.models import FeedBack
from .forms import (
    AddNewExerciseForm,
    EditUserDetailsForm,
    AddNewUserForm,
    FoodForm,
    ExerciseForm,
    EditFoodForm,
)
from django.http import HttpResponse
from caloricintake.models import CaloricIntake
from logworkout.models import Workout
from logmeasurements.models import BodyMeasurement
from reminders.models import Reminder


def adminlogin(request):
    """
    View function for handling admin login.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.

    """
    if request.method == "POST":
        # Handle POST request for authentication
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(user)
            if user.is_superuser:
                auth_login(request, user)
                return redirect("dashboard")

            return HttpResponse(
                "Not an admin user. Please login with admin credentials."
            )
        else:
            print(user)

            print(username, password)

            return HttpResponse("Invalid credentials. Please try again.")
    else:
        # Render login form for GET request
        return render(request, "login.html")


def login(request):
    """
    Renders the index.html template for the login page.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - A rendered HTML response.
    """
    return render(request, "index.html")


def dashboard(request):
    return render(request, "dashboard.html")


@login_required
def userpage(request):
    data = []
    common_users = CustomUser.objects.filter(is_superuser=False)
    for user in common_users:
        data.append(
            {
                "id": user.id,
                "fitness_level": user.fitness_level,
                "fitness_goal": user.fitness_goal,
                "age": user.age,
                "height": user.height,
                "weight": user.weight,
                "username": user.username,
                "name": user.name,
                "email": user.email,
                "password": user.password,
                "profile_picture": user.profile_picture,
                "is_verified": user.is_verified,
                "is_pro_member": user.is_pro_member,
            }
        )

    return render(request, "users.html", {"data": data})


@login_required
def exercises(request):
    data = []
    all_exercises = Exercise.objects.all()
    for exercise in all_exercises:

        if not exercise.added_by_user:
            uploader = "Admin"
        else:
            uploader = CustomUser.objects.get(id=exercise.uploaded_by)

        data.append(
            {
                "exercise_id": exercise.exercise_id,
                "name": exercise.exercise_name,
                "details": exercise.exercise_details,
                "image": exercise.exercise_image,
                "calories_burned_per_hour": exercise.calories_burned_per_hour,
                "added_by_user": exercise.added_by_user,
                "uploaded_by": uploader,
                "target_body_part": exercise.target_body_part.all(),
                "type": exercise.type,
            }
        )

    return render(request, "exercise.html", {"data": data})


@login_required
def food(request):
    # Query all food objects
    foods = Food.objects.all()

    # Create a list to store data of each food item
    data = []

    # Iterate over the queryset to access attributes of each food item
    for food in foods:

        data.append(
            {
                "id": food.id,
                "name": food.food_name,
                "description": food.food_description,
                "calories_per_serving": food.food_calories_per_serving,
                "serving_size": food.food_serving_size,
                "protein_per_serving": food.food_protein_per_servings,
                "carbs_per_serving": food.food_carbs_per_serving,
                "fat_per_serving": food.food_fat_per_serving,
                "image": food.food_image,
                "added_by_user": food.added_by_user,
                "uploaded_by": food.uploaded_by,
                # Add other attributes as needed
            }
        )

    return render(request, "food.html", {"data": data})


@login_required
def delete_item(request, item_id):

    try:
        # Get the item to be deleted
        item = get_object_or_404(Food, id=item_id)

        # Delete the item
        item.delete()

        messages.success(request, "Item deleted successfully.")
    except Food.DoesNotExist:
        messages.error(request, "Item not found.")

    # Redirect to the food page
    return redirect("food")


@login_required
def delete_exercise(request, exercise_id):
    try:
        # Get the item to be deleted
        item = get_object_or_404(Exercise, exercise_id=exercise_id)

        # Delete the item
        item.delete()

        messages.success(request, "Item deleted successfully.")
    except Exercise.DoesNotExist:
        messages.error(request, "Item not found.")
        return HttpResponse("Error Deleting Item.")

    # Redirect to the food page
    return redirect("exercises")


@login_required
def delete_user(request, user_id):
    try:
        # get user by id
        user = get_object_or_404(CustomUser, id=user_id)

        # delete the user
        user.delete()

    except CustomUser.DoesNotExist:
        messages.error(request, "User not found.")
        return HttpResponse("Error Deleting User.")

    return redirect("users")


def render_edit_page(request, item_id):
    try:
        food = Food.objects.get(id=item_id)
        if request.method == "POST":
            form = EditFoodForm(request.POST, request.FILES, instance=food)
            if form.is_valid():
                form.save()
                return redirect("render_edit_page", item_id=item_id)
        else:
            form = EditFoodForm(instance=food)
        return render(
            request, "edit_food.html", {"form": form, "food": food, "item_id": item_id}
        )
    except Food.DoesNotExist:
        return render(request, "error.html", {"error_message": "Food item not found."})
    except Exception as e:
        return render(request, "error.html", {"error_message": str(e)})


# @login_required
# def edit_food(request, item_id):
#     if request.method == "POST":
#         # Process form submission
#         food_id = item_id
#         food = Food.objects.get(pk=food_id)
#         food.food_name = request.POST.get("name")
#         food.food_price = request.POST.get("price")
#         food.food_description = request.POST.get("description")
#         food.food_image = request.POST.get("image")
#         food.save()
#         return redirect("list_foods")  # Redirect to the food list page after editing
#     else:
#         # Render edit form
#         food = Food.objects.get(pk=item_id)
#         context = {
#             "id": food.id,
#             "name": food.food_name,
#             "price": food.food_price,
#             "description": food.food_description,
#             "image": food.food_image.url if food.food_image else "",
#         }
#         return render(request, "edit_food.html", context)


@login_required
def edit_food(request, item_id):
    food = Food.objects.get(id=item_id)
    if request.method == "POST":
        form = EditFoodForm(request.POST, request.FILES)
        if form.is_valid():
            food.food_name = form.cleaned_data["food_name"]
            food.food_image = form.cleaned_data["food_image"]
            food.food_description = form.cleaned_data["food_description"]
            food.food_serving_size = form.cleaned_data["food_serving_size"]
            food.food_protein_per_servings = form.cleaned_data[
                "food_protein_per_servings"
            ]
            food.food_calories_per_serving = form.cleaned_data[
                "food_calories_per_serving"
            ]
            food.food_carbs_per_serving = form.cleaned_data["food_carbs_per_serving"]
            food.food_fat_per_serving = form.cleaned_data["food_fat_per_serving"]
            food.added_by_user = form.cleaned_data["added_by_user"]
            food.uploaded_by = form.cleaned_data["uploaded_by"]
            food.save()
            return redirect("render_edit_page")
        else:
            form = EditFoodForm(
                initial={
                    "food_name": food.food_name,
                    "food_image": food.food_image,
                    "food_description": food.food_description,
                    "food_serving_size": food.food_serving_size,
                    "food_protein_per_servings": food.food_protein_per_servings,
                    "food_calories_per_serving": food.food_calories_per_serving,
                    "food_carbs_per_serving": food.food_carbs_per_serving,
                    "food_fat_per_serving": food.food_fat_per_serving,
                    "added_by_user": food.added_by_user,
                    "uploaded_by": food.uploaded_by,
                }
            )

        return render(
            request, "edit_food.html", {"form": form, "food": food, "item_id": item_id}
        )


@login_required
def edit_user(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    if request.method == "POST":
        form = EditUserDetailsForm(request.POST)
        if form.is_valid():
            # Process the form data
            # Update the user object with the form data
            user.username = form.cleaned_data["username"]
            user.name = form.cleaned_data["name"]
            user.email = form.cleaned_data["email"]
            user.fitness_level = form.cleaned_data["fitness_level"]
            user.fitness_goal = form.cleaned_data["fitness_goal"]
            user.age = form.cleaned_data["age"]
            user.height = form.cleaned_data["height"]
            user.weight = form.cleaned_data["weight"]
            user.is_verified = form.cleaned_data["is_verified"]
            user.is_pro_member = form.cleaned_data["is_pro_member"]
            user.save()
            return redirect("profile", user_id=user_id)  # Redirect to profile page
    else:
        form = EditUserDetailsForm(
            initial={
                "username": user.username,
                "name": user.name,
                "email": user.email,
                "fitness_level": user.fitness_level,
                "fitness_goal": user.fitness_goal,
                "age": user.age,
                "height": user.height,
                "weight": user.weight,
                "is_verified": user.is_verified,
                "is_pro_member": user.is_pro_member,
            }
        )
    return render(request, "edit_user.html", {"form": form, "user": user})


@login_required
def render_edit_exercise_page(request, item_id):
    try:
        exercise = Exercise.objects.get(pk=item_id)
        if request.method == "POST":
            form = ExerciseForm(request.POST, request.FILES, instance=exercise)
            if form.is_valid():
                form.save()
                return redirect("exercises")
        else:
            form = ExerciseForm(instance=exercise)
        return render(
            request,
            "edit_exercise.html",
            {"form": form, "exercise": exercise, "item_id": item_id},
        )
    except Exercise.DoesNotExist:
        return render(request, "error.html", {"error_message": "Exercise not found."})
    except Exception as e:
        return render(request, "error.html", {"error_message": str(e)})


@login_required
def edit_exercise(request, item_id):
    try:
        exercise = Exercise.objects.get(exercise_id=item_id)

        if request.method == "POST":
            form = ExerciseForm(request.POST, request.FILES)
            if form.is_valid():
                exercise.exercise_name = form.cleaned_data["exercise_name"]
                exercise.exercise_details = form.cleaned_data["exercise_details"]
                exercise.exercise_image = form.cleaned_data["exercise_image"]
                exercise.calories_burned_per_hour = form.cleaned_data[
                    "calories_burned_per_hour"
                ]
                exercise.added_by_user = form.cleaned_data["added_by_user"]
                exercise.uploaded_by = form.cleaned_data["uploaded_by"]
                exercise.save()
                return redirect("exercises")
            else:
                form = ExerciseForm(
                    initial={
                        "exercise_name": exercise.exercise_name,
                        "exercise_details": exercise.exercise_details,
                        "exercise_image": exercise.exercise_image,
                        "calories_burned_per_hour": exercise.calories_burned_per_hour,
                        "added_by_user": exercise.added_by_user,
                        "uploaded_by": exercise.uploaded_by,
                    }
                )
            return render(
                request, "edit_exercise.html", {"form": form, "exercise": exercise}
            )
        else:

            return HttpResponse("Method not allowed", status=405)
    except Exercise.DoesNotExist:
        return HttpResponse("Exercise not found", status=404)
    except Exception as e:
        print(e)
        return render(request, "error.html", {"error": str(e)})


@login_required
def view_profile(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    email = CustomUser.objects.get(id=user_id).email
    request.session["email"] = email
    return render(request, "profile.html", {"user": user})


def add_new_user(request):
    return render(request, "add_new_user.html", {"form": AddNewUserForm()})


def register_new_user(request):
    if request.method == "POST":
        form = AddNewUserForm(request.POST, request.FILES)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data["password"]
            )  # Ensure your form has a password field
            new_user.save()
            messages.success(request, "User added successfully")
            return redirect("dashboard")  # Ensure you have a URL name 'dashboard'
        else:

            messages.error(request, "Error adding user")
            # Return the same page with form errors
            return render(request, "add_new_user.html", {"form": form})
    else:
        form = AddNewUserForm()
        return render(request, "add_new_user.html", {"form": form})


def alter_user_details(request, username):
    if request.method == "POST":
        try:

            user = CustomUser.objects.get(username=username)

            form = EditUserDetailsForm(request.POST, request.FILES, instance=user)

            if form.is_valid():
                # Save the form data without checking uniqueness constraints
                form.save(commit=False)
                form.save()

                return redirect("view_profile", user_id=user.id)
            else:

                print(form.errors)
                return HttpResponse(f"Invalid form data{form.errors}")

        except CustomUser.DoesNotExist:
            return HttpResponse("User not found")
        except Exception as e:

            return HttpResponse(f"An error occurred: {str(e)}")
    else:
        return HttpResponse("Invalid request method")


def navigate_to_add_food(request):
    form = FoodForm()
    return render(request, "add_new_food.html", {"form": form})


def navigate_to_add_exercise(request):
    form = AddNewExerciseForm()
    return render(request, "add_new_exercise.html", {"form": form})


def add_new_exercise(request):
    try:
        if request.method == "POST":
            form = ExerciseForm(request.POST, request.FILES)
            if form.is_valid():
                exercise = form.save(commit=False)
                exercise.type = form.cleaned_data[
                    "type"
                ]  # Assign the ExerciseType object
                exercise.save()  # Assign the ID to the type_id field

                return redirect("dashboard")
        else:
            form = ExerciseForm()
        return render(request, "add_new_exercise.html", {"form": form})

    except Exception as e:
        print(e)
        return render(request, "error.html", {"error_message": str(e)})


def add_new_food(request):
    try:
        if request.method == "POST":
            form = FoodForm(request.POST, request.FILES)
            if form.is_valid():
                new_food = form.save(commit=False)
                new_food.added_by_user = False
                new_food.save()
                messages.success(request, "Food added successfully")
                return redirect("dashboard")  # Ensure you have a URL name 'food'
            else:
                messages.error(request, "Error adding food")
                # Return the same page with form errors
                return render(request, "add_new_food.html", {"form": form})
        else:
            form = FoodForm()
            return render(request, "add_new_food.html", {"form": form})

    except Exception as e:
        print(e)
        return HttpResponse("Error adding food")


def navigate_to_send_email(request):
    email = request.session.get("email")
    return render(request, "send_email.html", {"email": email})


def naviagte_to_send_all_email(request):

    return render(
        request,
        "send_mail_all.html",
    )


def navigate_to_user_view_options(request, id):

    return render(request, "user_options.html", {"id": id})


def get_caloric_intake(request, id):
    caloric_intakes = CaloricIntake.objects.filter(username=id)
    return render(
        request, "user_view_caloricintake.html", {"caloric_intakes": caloric_intakes}
    )


def get_workout_data(request, id):
    workouts = Workout.objects.filter(username=id)
    return render(request, "user_view_workouts.html", {"workouts": workouts})


def get_user_measurements(request, id):
    measurements = BodyMeasurement.objects.filter(user=id)
    return render(
        request, "user_view_measurements.html", {"measurements": measurements}
    )


def get_user_reminders(request, id):
    reminders = Reminder.objects.filter(user=id)
    return render(request, "user_view_reminders.html", {"reminders": reminders})


def render_please_login(request):
    return render(request, "please_login.html")


def render_subscription_page(request):
    subscriptions = Subscription.objects.all()

    return render(
        request, "view_all_subscription.html", {"subscriptions": subscriptions}
    )


def render_push_notificatoin(request):
    return render(request, "push_notification.html")


def render_see_allFeedbacks(request):
    feedbacks = FeedBack.objects.all()

    return render(request, "see_user_feedbacks.html", {"feedbacks": feedbacks})
