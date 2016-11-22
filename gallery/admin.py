from ckeditor.widgets import CKEditorWidget
from django import forms

from django.contrib import admin

from .models import Picture, Album, Video
# Register your models here.


class InlinePicture(admin.TabularInline):
    model = Picture


class AlbumAdmin(admin.ModelAdmin):
    inlines = [InlinePicture]


class VideoContentForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Video
        fields = '__all__'


class VideoAdmin(admin.ModelAdmin):
    form = VideoContentForm


admin.site.register(Video, VideoAdmin)
admin.site.register(Album, AlbumAdmin)