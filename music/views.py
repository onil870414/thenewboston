from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>This will be a list  of all albums</h1>')

def detail(request, album_id):
    return HttpResponse(f'<h1>Details for album id: {album_id} </h1>')