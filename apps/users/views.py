from django.shortcuts import render
from django.contrib import messages
from .models import User
from django.conf import settings
from django.core.validators import validate_email
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
import re
from django.conf import settings
from .appwrite_client import appwrite_client
from .forms import *
from django.contrib.auth import (authenticate,
                                 login,
                                 logout
                                )
from django.shortcuts import render, redirect, get_object_or_404


def index_page(request):
    return render(request, 'index.html')


def register_view(request): # Creates a New Account & login New users
    if request.user.is_authenticated:
        return redirect("index")
    else:
        form = UserRegistrationForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password1")
            user.set_password(password)
            connect_appwrite = appwrite_client()
            databases = connect_appwrite[0]
            document_id = connect_appwrite[1]   #appwrite
            user_data = {
                'username': form.cleaned_data['username'],
                'email': form.cleaned_data['email'],
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'bio': form.cleaned_data['bio']
            }
            databases.create_document(    
                database_id=settings.APPWRITE_DATABASE_ID,
                collection_id=settings.APPWRITE_DOCUMENT_ID,
                document_id=document_id,
                data=user_data
            )                                   
            user.save()
            new_user = authenticate(email=user.email, password=password)
            login(request, new_user)
            return redirect("index")

        context = {"form":form}

        return render(request, "signup.html", context)
    

def login_view(request): # users will login with their Email & Password
    if request.user.is_authenticated:
        return redirect("index")
    else:
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            # authenticates Email & Password
            user = authenticate(email=email, password=password) 
            login(request, user)
            return redirect("index")
        context = {"form":form}

        return render(request, "login.html", context)
    
def logout_view(request): # logs out the logged in users
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        logout(request)
        return redirect("index")


def user_profile(request, username=None): # Displays User Profile
    user_profile = get_object_or_404(User, username=username)
    context = { "user_profile": user_profile, 
              }
    return render(request, "dashboard.html", context)