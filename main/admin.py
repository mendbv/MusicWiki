from django.contrib import admin

from .models import Group, Album, Song, GroupMember


@admin.register(Group)
class AdminGroup(admin.ModelAdmin):
    list_display = ['id', 'name', 'creation_date']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'description']


@admin.register(Album)
class AdminAlbum(admin.ModelAdmin):
    list_display = ['id', 'name', 'group', 'release_date']
    list_display_links = ['id', 'name']
    list_filter = ['group', 'release_date']
    search_fields = ['name', 'description']


@admin.register(Song)
class AdminSong(admin.ModelAdmin):
    list_display = ['id', 'name', 'album', 'group', 'duration']
    list_display_links = ['id', 'name']
    list_filter = ['album', 'group']
    search_fields = ['name', 'lyrics']


@admin.register(GroupMember)
class AdminGroupMember(admin.ModelAdmin):
    list_display = ['id', 'name', 'role', 'group']
    list_display_links = ['id', 'name']
    list_filter = ['group', 'role']
    search_fields = ['name', 'biography']
