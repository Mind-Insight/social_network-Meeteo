from django.urls import path

from . import views


app_name = "publications"
urlpatterns = [
    path("", views.publications_list, name="publications_list"),
    path(
        "publication/<slug:publication_slug>/",
        views.publication_detail,
        name="publication_detail",
    ),
    path("add_post", views.add_post, name="add_post"),
]
