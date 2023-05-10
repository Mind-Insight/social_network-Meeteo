from django.shortcuts import render


def user_profile(request):
    return render(request, 'users/user_profile.html')


def register(request):
    return render(request, 'users/register.html')


def login(request):
    return render(request, 'users/login.html')