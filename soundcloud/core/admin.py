from django.contrib import admin
from .models import Artist, Genre, Album, Track, PlayList

admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(PlayList)

