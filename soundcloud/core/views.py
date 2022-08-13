from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Artist, Album, Track




class HomeView(View):
    def get(self, request):
        context = {'artist_list': Artist.objects.all(), 'track_list': Track.objects.all()}
        return render(request, 'index.html', context=context)


class Artist_detail(DetailView):
    model = Artist
    slug_field = "url"
    context_object_name = 'artists'
    template_name = "main/artist.html"


class Artist_list(View):
    pass


class Album_detail(DetailView):
    model = Album
    slug_field = "url"
    context_object_name = 'releases'
    template_name = "main/release.html"


class Album_list(ListView):
    def get(self, request):
        album = Album.objects.all()
        return render(request, 'main/releases.html', {"album_list": album})


class Tracks_detail(DetailView):
    model = Track
    slug_field = "url"
    context_object_name = 'tracks'
    template_name = "include/test.html"
