from django.contrib import admin
import time


from .models import Album, Song, Artist


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('release_date', )
    search_fields = ('name', 'artist_name')
    list_display = ('id', 'name', 'artist_name', 'release_date', 'production_house')
    list_editable = ('production_house', )


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    save_on_top = True
    #exclude = ('lyrics', )
    #autocomplete_fields = ['album']
    list_display = ("id",'album', 'name', "duration", "lyrics")
    list_editable = ('name', )
    search_fields = ('album', )
    list_filter = ('name', 'album__name', 'album__artist_name')
    search_fields = ['album']

    def duration_human_readable(self, obj):
        return time.strftime("%M:%S", time.gmtime(obj.duration))

    duration_human_readable.short_description = 'Duration'
    duration_human_readable.admin_order_field = 'duration'


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):

    list_display = ('id', 'music_type', 'name')
    list_editable = ('name', )






#admin.site.register(Album, AlbumAdmin)
#admin.site.register(Song, SongAdmin)
#admin.site.register(Artist)

# Register your models here.
