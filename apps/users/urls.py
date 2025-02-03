from django.urls import path
from .views import *

urlpatterns = [
    path('register', register_view, name="signup"),
    path('login', login_view, name="login"),
    path('logout', logout_view, name="logout"),
    path('', index_page, name="index"),
    path('profile/str:<username>', user_profile, name="user_profile"),
]
