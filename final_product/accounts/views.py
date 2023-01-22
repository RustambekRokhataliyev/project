from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from .forms import UserRegistrationForm, UserAuthenticationForm


# Create your views here.


def user_login(request):
    if request.method == "POST":
        form = UserAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
    else:
        form = UserAuthenticationForm()

    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context)


def registration_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegistrationForm()
    context = {
        "form": form
    }
    return render(request, "accounts/registration.html", context)


def user_logout(request):
    logout(request)
    return redirect("index")
