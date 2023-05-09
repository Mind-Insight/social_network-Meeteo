from django.urls import path

from . import views


app_name = 'friends'
urlpatterns = [
    path('', views.friends_list, name='friends_list'),
]