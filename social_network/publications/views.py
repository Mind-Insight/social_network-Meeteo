from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)
from django.utils.text import slugify
from unidecode import unidecode
from django.db.models import Q
from .forms import AddPostForm

from .models import Publication


def publications_list(request):
    publications = Publication.objects.filter(is_public=True)
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


def add_post(request):
    if request.method != "POST":
        form = AddPostForm()
    else:
        form = AddPostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            title = form.cleaned_data.get('title')
            new_post.slug = slugify(unidecode(title))
            new_post.save()
            return redirect("publications:publications_list")

    context = {
        "form": form,
    }
    return render(request, "publications/add_post.html", context)
