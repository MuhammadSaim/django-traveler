from django.contrib.auth.views import auth_logout
from django.urls import path

from . import views


urlpatterns = [
    path('login', views.login_view, name="login"),
    path('register', views.register_view, name="register"),
    path('logout', views.logout_view, name="logout"),
    path('profile', views.user_profile_view, name="profile"),
]