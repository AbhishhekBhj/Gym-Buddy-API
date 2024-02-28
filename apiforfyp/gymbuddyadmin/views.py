from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def adminlogin(request):
    if request.method == "POST":
        # Handle POST request for authentication
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return HttpResponse("User authenticated and logged in")
        else:
            return HttpResponse("Invalid credentials")
    else:
        # Render login form for GET request
        return render(request, "login.html")


def login(request):
    return render(request, "index.html")


# return adminlogin(request)
