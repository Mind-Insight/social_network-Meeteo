from django.urls import path

from . import views


urlpatterns = [
    path('', views.description, name='description'),
]