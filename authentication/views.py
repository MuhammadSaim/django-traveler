from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import (
    authenticate,
    login,
    logout
)
from django.core.paginator import Paginator
from authentication.forms.UserLoginForm import UserLoginForm
from authentication.forms.UserRegisterForm import UserRegisterForm
from authentication.forms.UserProfileForm import UserProfileForm
from .models import User
from django.contrib import messages


# login view for user login
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')
    return render(request, 'authentication/login.html', {'form': form})


# register view for register user
def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'authentication/register.html', context)


# logout user
def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('home')
    logout(request)
    return redirect('login')


# user's profile view
@login_required
def user_profile_view(request):
    user = User.objects.filter(id=request.user.id).first()
    form = UserProfileForm(request.POST or None, request.FILES or None, instance=user)
    if form.is_valid():
        form.save(commit=True)
        messages.add_message(request, messages.SUCCESS, "Your Profile is updated successfully.")
    context = {
        'form': form
    }
    return render(request, "authentication/profile.html", context)


@login_required
def manage_users(request):
    if request.user.role == 'admin':
        users = User.objects.all().order_by('-id')
        paginator = Paginator(users, per_page=10)
        page_number = request.GET.get('page')
        users = paginator.get_page(page_number)
        context = {
            'users': users
        }
        return render(request, 'authentication/users.html', context)


@login_required
def user_status(request, id):
    if request.user.role == 'admin':
        user = get_object_or_404(User, id=id)
        if user.is_active:
            user.is_active = False
        else:
            user.is_active = True
        user.save(update_fields=['is_active'])
        return redirect('users')


@login_required
def user_delete(request, id):
    if request.user.role != 'admin':
        return redirect('home')
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('users')
