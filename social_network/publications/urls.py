from django.urls import path

from . import views


app_name = 'publications'
urlpatterns = [
    path('', views.publications_list, name='publications_list'),
    path('<int:publication_id>/', views.publication_detail, name='publication_detail'),
]
