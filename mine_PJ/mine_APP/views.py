from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView

from mine_APP.forms import AddMusicForm, PlayListForm
from mine_APP.models import music, Genre, History, PlayList, Album


# Create your views here.


@method_decorator(login_required(login_url='login_page'), name='dispatch')
class HomeView(ListView):
    template_name = 'mine_APP/main.html'
    model = Genre
    context_object_name = 'genres'


@method_decorator(login_required(login_url='login_page'), name='dispatch')
class GenreDetailView(DetailView):
    model = Genre
    context_object_name = 'genre'
    template_name = 'mine_APP/genre_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        genre = context.get('genre')
        context['musics'] = genre.musics.all()  # получаем все музыки данного жанра с помощ  ью related_name
        return context


@method_decorator(login_required(login_url='login_page'), name='dispatch')
class MusicDetailView(DetailView):
    model = music
    context_object_name = 'music'
    template_name = 'mine_APP/music_detail.html'


    def post(self,request, *args, **kwargs):
        musics = music.objects.get(pk=self.kwargs['pk'])
        playlist = self.request.POST['playlist']
        playlist_obj = PlayList.objects.get(pk=playlist)
        playlist_obj.musics.add(musics) # добавляем музыку в плейлист
        return super().get(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        History.objects.create(music=music.objects.get(pk=self.kwargs['pk']),
                               user=self.request.user)  # сохраняем в историй
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        music = context.get('music')
        genres = music.genres.all()  # получаем все жанры данной музы
        context['genres'] = genres  # получаем все музыки, связанные с текущей
        context['genres_str'] = ', '.join(map(lambda genre: genre.name, genres))  # конвертируем queryset в список
        context['playlists'] = self.request.user.playlists_au.all()  # получаем все плейлисты
        return context


@method_decorator(login_required(login_url='login_page'), name='dispatch')
class HistoryView(ListView):
    model = History
    context_object_name = 'histories'
    paginate_by = 4  # указание на то сколько записей выводить на странице (для пагинаций)
    template_name = 'mine_APP/history.html'

    # Получение истории пользователя
    def get_queryset(self):
        return History.objects.filter(user=self.request.user).order_by('-listned_at')


@method_decorator(staff_member_required(login_url='login_page'), name='dispatch')
class MusicAddView(CreateView):
    template_name = 'mine_APP/Music_add.html'
    model = music
    form_class = AddMusicForm  # указываем используемый форм-класс

    def form_valid(self, form):
        music = form.save(commit=False)
        music.author = self.request.user
        music.save()
        form.save_m2m()  # сохраняем связанные данные ()
        return redirect('home')


@method_decorator(login_required(login_url='login_page'), name='dispatch')
class PlayListView(ListView):
    model = PlayList
    context_object_name = 'playlists'
    template_name = 'mine_APP/playlists.html'

    def get_queryset(self):
        return PlayList.objects.filter(author=self.request.user).order_by('-created_at')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        new_playlists = []
        for playlist in ctx['playlists']:
            musics = playlist.musics.all()
            new_playlist = {
                'name': playlist.name,
                'id': playlist.id,
                'created_at': playlist.created_at,
                'images': musics[0].image if len(musics) > 0 else None,
            }
            new_playlists.append(new_playlist)
        ctx['new_playlists'] = new_playlists
        ctx['form'] = PlayListForm()  # форма для создания нового плейлист
        return ctx

    def post(self, *args, **kwargs):
        form = PlayListForm(self.request.POST)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.author = self.request.user
            playlist.save()
        return super().get(*args, **kwargs)

@method_decorator(login_required(login_url='login_page'), name='dispatch')
class PlaylistDetailView(DetailView):
    template_name = 'mine_APP/playlist_detail.html'
    model = PlayList
    context_object_name = 'playlist'

    def get(self,request, *args, **kwargs):
        playlist = PlayList.objects.get(pk=self.kwargs['pk'])
        if request.user.id != playlist.author.id: # проверяем, является ли текущий пользователь владелец
            if not playlist.is_public: # если не публичный, возвращаем ошибку
                return redirect('error')
        return super().get(request, *args, **kwargs)

    # удаляем музыку из плейлиста
    def post(self, request, *args, **kwargs):
        playlist = PlayList.objects.get(pk=self.kwargs['pk']) # получаем плейлист по id
        music_id = self.request.POST['music_id'] # получаем id музыки
        musics = music.objects.get(pk=music_id)
        print(1)
        # получаем музыку по id
        if request.user.id != playlist.author.id:
            return redirect('error')
        playlist.musics.remove(musics) # удаляем музыку из плейлиста
        print(2)
        return super().get(request, *args, **kwargs) # возвращаемся на страницу плейлиста

@method_decorator(login_required(login_url='login_page'), name='dispatch')
class PlayListDeleteView(DeleteView):
    model = PlayList
    template_name = 'mine_APP/playlist_delete.html'
    context_object_name = 'playlist'
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        playlist = PlayList.objects.get(pk=self.kwargs['pk'])
        if request.user.id != playlist.author.id:
            return redirect('error')
        playlist.delete()
        return redirect('playlists')

@method_decorator(login_required(login_url='login_page'), name='dispatch')
class AlbumView(ListView):
    template_name ='mine_APP/albums.html'
    model = Album
    context_object_name = 'albums'


@method_decorator(login_required(login_url='login_page'), name='dispatch')
class AlbumDetailView(DetailView):
    model = Album
    context_object_name = 'album'
    template_name = 'mine_APP/album_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        album = context.get('album')
        context['musics'] = album.musics.all()
        return context

    def post(self, request, *args, **kwargs):
        album = Album.objects.get(pk=self.kwargs['pk']) # получаем альбом по id
        music_id = music.objects.get(pk=self.request.POST['music_album']) # получаем id музыки
        if request.user.id != album.author.id: # проверяем, является ли текущий пользователь владеле
            return redirect('error')
        album.musics.remove(music_id) #  удаляем музыку из альбома
        return redirect('album_detail', pk=album.id) # возвращаемся на страницу альбома 
