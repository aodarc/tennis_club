from django.contrib import admin

from .models import Picture, Album
# Register your models here.


class InlinePicture(admin.TabularInline):
    model = Picture


class AlbumAdmin(admin.ModelAdmin):
    inlines = [InlinePicture]

admin.site.register(Album, AlbumAdmin)