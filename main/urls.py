from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('groups/', views.get_groups, name='groups'),
    path('group/<int:pk>/', views.get_group_detail, name='group_detail'),
    path('album/<int:pk>/', views.get_album_detail, name='album_detail'),
    path('song/<int:pk>/', views.get_song_detail, name='song_detail'),
    path('member/<int:pk>/', views.get_member_detail, name='member_detail'),
    path('songs/', views.get_songs, name='songs'),
    path('albums/', views.get_albums, name='albums'),
]
