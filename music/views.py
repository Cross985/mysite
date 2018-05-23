from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Album,Song
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.urls import reverse

# Create your views here.
def index(request):
    # album_list = Album.objects.order_by('album_title')[:0]
    # output = ','.join([a.album_title for a in album_list])
    # return HttpResponse(output)
    album_list = Album.objects.order_by('album_title')[:5]
    template = loader.get_template('music/index.html')
    context = {
        'album_list':album_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request,'music/index.html',context)


def detail(request, album_id):
    # try:
    #     album = Album.objects.get(id=album_id)
    # except Album.DoesNotExist:
    #     raise Http404('Album is not exist.')
    # # response = "You are looking at the detail of Album %s."
    # # return HttpResponse(response % album_id)
    # return render(request,'music/detail.html',{'album':album})

    album = get_object_or_404(Album,id=album_id)
    songs = album.related_song_record.all()
    return render(request,'music/detail.html',{'album':album})

def song_detail(request,song_id):

    song=get_object_or_404(Song,id=song_id)
    return render(request,'music/song_detail.html',{'song':song, 'error_message': None})

def save_song(request,song_id):
    song = get_object_or_404(Song,id=song_id)
    try:
        radio = request.POST['name']
    except (KeyError):
        raise Http404('None was chosen.')
    if radio == '1':
        song.song_title = song.song_title + 'test'
        song.save()
    # return render(request,'music/song_detail.html',{'song':song,'error_message': None})
    return  HttpResponseRedirect(reverse('music:song_detail', args=(song.id,)))

from django.views import generic

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'album_list'#需要与template中的context name相同
    model = Album

    def get_queryset(self):
        return Album.objects.order_by('album_title')[:5]


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class SongView(generic.DetailView):
    model = Song
    template_name = 'music/song_detail.html'