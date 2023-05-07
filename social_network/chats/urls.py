from django.urls import path

from . import views


app_name = 'chats'
urlpatterns = [
    path('', views.chats_list, name='chats_list'),
]