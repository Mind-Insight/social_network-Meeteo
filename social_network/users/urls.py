from django.urls import path

from . import views


app_name = 'users'
urlpatterns = [
    path('profile/', views.user_profile, name='user_profile'),
    path('registration/', views.register, name='register'),
    path('login/', views.login, name='login'),
]
