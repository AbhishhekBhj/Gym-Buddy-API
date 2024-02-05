from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from users.models import CustomUser as User
from django.views import View


def admin_login(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate the user
        user_auth = authenticate(username=username, password=password)

        if user_auth is not None:
            if user_auth.is_superuser:
                login(request, user_auth)
                return redirect("dashboard")
            else:
                messages.info(request, "Invalid Credentials")
        else:
            messages.info(request, "Invalid Credentials")

    return redirect("login")  # Use the correct URL name for your login view


def login(
    request,
):
    return render(request, "customadmin/login.html", {})


def dashboard(request):
    return render(request, "customadmin/dashboard.html")
