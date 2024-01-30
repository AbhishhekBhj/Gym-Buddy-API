from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from users.models import CustomUser as User


class AdminView:
    def admin_login(request):
        
            if request.user.is_authenticated:
                return redirect("/dashboard/")
            if request.method=="POST":
                username = request.POST.get("username")
                password = request.POST.get("password")
                user_obj = User.objects.filter(username=username)
                if not user_obj.exists():
                    messages.info(request,"User not found")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                
                user_obj = authenticate(username=username,password=password)
                
                
                #if uses is admin
                if user_obj and user_obj.is_superuser:
                    login(request,user_obj)
                    return redirect("/dashboard/")
                
                
                
                messages.info(request,"Invalid Credentials")
                return  redirect("/")
            
            
            return render(request,"login.html")