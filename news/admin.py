from django.contrib import admin
from django import forms

from ckeditor.widgets import CKEditorWidget

from .models import News, Image, Tag


# Register your models here.


class NewsContentForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = NewsContentForm


admin.site.register(Image)
admin.site.register(Tag)
admin.site.register(News, NewsAdmin)
