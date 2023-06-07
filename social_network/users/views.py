from django.shortcuts import render, redirect
from .forms import RegisterForm


def user_profile(request):
    context = {}
    return render(request, "users/user_profile.html", context)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect("/")
    else:
        form = RegisterForm()

    context = {
        "form": form,
    }
    return render(request, "users/register.html", context)


def login(request):
    return render(request, "users/login.html")
