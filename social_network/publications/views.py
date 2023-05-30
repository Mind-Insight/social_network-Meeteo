from django.shortcuts import render

from .models import Publication


def publications_list(request):
    publications = Publication.objects.all()
    context = {
        "publications": publications,
        "title": "Publications",
    }
    return render(request, "publications/publications_list.html", context)


def publication_detail(request, publication_id):
    publication = Publication.objects.get(pk=publication_id)
    context = {
        "title": "publication",
        "publication": publication,
    }
    return render(request, "publications/publication_detail.html", context)
