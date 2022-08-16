from django.contrib.auth.views import auth_logout
from django.urls import path

from . import views


urlpatterns = [
    path('login', views.login_view, name="login"),
    path('register', views.register_view, name="register"),
    path('logout', views.logout_view, name="logout"),
    path('profile', views.user_profile_view, name="profile"),
    path('users', views.manage_users, name="users"),
    path('forgot-password', views.forgot_password_view, name="forgot.password"),
    path('reset-password', views.reset_password_view, name="reset.password"),
    path('users/status/<int:id>', views.user_status, name="user.status"),
    path('users/delete/<int:id>', views.user_delete, name="user.delete"),
]