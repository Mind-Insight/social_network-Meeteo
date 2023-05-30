from django.shortcuts import render, get_object_or_404

from .models import Publication


def publications_list(request):
    # publications = get_list_or_404(Publication)
    publications = Publication.objects.all()
    context = {
        "publications": publications,
        "title": "Publications",
    }
    return render(request, "publications/publications_list.html", context)


def publication_detail(request, publication_slug):
    publication = get_object_or_404(Publication, slug=publication_slug)
    context = {
        "title": "publication",
        "publication": publication,
    }
    return render(request, "publications/publication_detail.html", context)
