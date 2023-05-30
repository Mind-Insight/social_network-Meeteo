from django.contrib import admin

from .models import Publication, Friend, Profile, Comment


class PublicationAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "main",
        "user",
        "is_public",
    )

    list_editable = ("is_public",)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Publication, PublicationAdmin)
admin.site.register(Friend)
admin.site.register(Profile)
admin.site.register(Comment)
