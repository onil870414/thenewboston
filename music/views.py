from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from music.models import Album

def index(request):
    all_albums = Album.objects.all()
    html = ''
    for album in all_albums:
        url = 'music/'
    return HttpResponse('')

def detail(request, album_id):
    try:
        album = Album.objects.get(id = album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")

    return render(request, 'details.html', {'album' : album})