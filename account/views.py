from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model, logout, authenticate
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import (
    RegisterForm,
    LoginForm,
    ProfileForm,
)

User = get_user_model()


def register_view(request):
    form = RegisterForm(request.POST or None)
    # Call clean function in forms
    if form.is_valid():
        # Get input from user
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")

        # Create user and user profile
        user = User.objects.create_user(username, email, password)
        Profile.objects.create(user=user)

        login(request, user)
        return redirect("portfolio:homepage")
    return render(request, "account/register_page.html", {"form": form})


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect("portfolio:homepage")
    return render(request, "account/login_page.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("account:login")


@login_required(login_url='account:login')
def profile_view(request):
    user = request.user.profile
    form = ProfileForm(instance=user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("portfolio:homepage")
    return render(request, "account/profile_page.html", {"form": form})
