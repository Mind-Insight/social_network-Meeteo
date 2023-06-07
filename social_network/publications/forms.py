from django import forms

from .models import Publication


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = [
            "title",
            "main",
            "image",
            "is_public",
        ]
