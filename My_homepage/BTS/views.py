from django.views.decorators.http import require_http_methods, require_POST
from django.shortcuts import redirect, render, get_object_or_404
from .models import Artist , Albums , songs
from .forms import ArtistForm , AlbumsForm

# Create your views here.

def index(request) :
    BTS = Artist.objects.order_by('-pk')

    context = {
        'BTS' : BTS,
    }

    return render(request,'BTS/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request) :
    # create창에서 제출버튼을 눌러서 db에 저장하려고 할때
    if request.method == "POST":
        form = ArtistForm(request.POST, files=request.FILES) # 받아온 데이터 form형태로 저장
        if form.is_valid():
            member = form.save()
            return redirect('BTS:detail', member.pk)

    else :
        # create창에 들어와서 글을 작성하려할 때
        form = ArtistForm()
    context = {
        'form' : form,
    }
    return render(request, 'BTS/create.html', context)

def detail(request,pk) :
    member = get_object_or_404(Artist,pk=pk)
    context = {
        'member' : member,
    }
    return render(request, 'BTS/detail.html',context)
    
@require_http_methods(['GET', 'POST'])
def update(request, pk) :
    member = get_object_or_404(Artist, pk=pk)
    if request.method == "POST" :
        form = ArtistForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return redirect('BTS:detail', member.pk) # view안에서 이동!

    # detail에서 불려졌을 때
    else :
        form = ArtistForm(instance=member)
    context ={
        'member' : member ,
        'form' : form,
    }

    return render(request, 'BTS/update.html', context)

@require_POST
def delete(request, pk) :
    member = get_object_or_404(Artist,pk=pk) # 데이터를 들오고는 거지, form을 들고오는게 아니므로
    member.delete()
    return redirect('BTS:index')


# 앨범 게시판
def album_index(request) :
    albums = Albums.objects.order_by('-pk')

    context = {
        'albums' : albums,
    }

    return render(request,'BTS/album_index.html', context)


def album_index_create(request) :
    if request.method == "POST":
        form = AlbumsForm(data = request.POST, files = request.FILES) # 받아온 데이터 form형태로 저장
        if form.is_valid():
            album = form.save()
            return redirect('BTS:album_detail', album.pk)
    else :
    # create창에 들어와서 글을 작성하려할 때
        form = AlbumsForm()
    context = {
        'form' : form,
    }
    return render(request, 'BTS/album_index_create.html', context)


def album_detail(request, pk):
    album = get_object_or_404(Albums,pk=pk)
    # album_songs = get_object_or_404(songs, album_fk_id=pk)
    # for song in songs :
    #     if pk == song.album_fk_id :
    #         print(f'{songs.objects.)}')
    album_songs = songs.objects.filter(album_fk_id=pk)
    print(album_songs)
    context = {
        'album' : album,
        'album_songs' : album_songs,
    }
    return render(request, 'BTS/album_detail.html',context)


