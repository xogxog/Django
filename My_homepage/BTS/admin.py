from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Artist , Albums, songs

# Register your models here.

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('pk','name','birth','height')

class AlbumsAdmin(admin.ModelAdmin):
    list_display = ('pk','title','released','singer', 'album_cover')

class songsAdmin(admin.ModelAdmin):
    list_display = ('album_fk', 'title','singer')

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Albums, AlbumsAdmin)
admin.site.register(songs, songsAdmin)