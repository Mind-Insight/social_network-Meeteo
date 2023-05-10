from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('publications.urls')),
    path('chats/', include('chats.urls')),
    path('about/', include('about.urls')),
    path('', include('users.urls')),
    path('friends/', include('friends.urls')),
]
