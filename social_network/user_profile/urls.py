from django.urls import path

from . import views


app_name = 'profile'
urlpatterns = [
    path('', views.user_profile, name='user_profile'),
]