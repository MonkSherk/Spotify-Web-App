from django.urls import path
from django.views.generic import TemplateView

from mine_APP import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('genre/<int:pk>', views.GenreDetailView.as_view(), name='genre_detail'),
    path('music/<int:pk>', views.MusicDetailView.as_view(), name='music_detail'),
    path('history/', views.HistoryView.as_view(), name='history'),
    path('upload_music/', views.MusicAddView.as_view(), name='upload_music'),
    path('playlists/', views.PlayListView.as_view(), name='playlists'),
    path('playlist_detail/<int:pk>', views.PlaylistDetailView.as_view(), name='playlist_detail'),
    path('playlist_delete/<int:pk>', views.PlayListDeleteView.as_view(), name='playlist_delete'),
    path('album_view/', views.AlbumView.as_view(), name='album_page') ,
    path('album_detail/<int:pk>', views.AlbumDetailView.as_view(), name='album_detail'),
    path('error/',TemplateView.as_view(template_name='mine_APP/error_mes.html'), name='error')
]


