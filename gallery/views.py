from django.views.generic import TemplateView
from news.models import News

from .models import Album, Video


# Create your views here.


class GalleryView(TemplateView):
    template_name = 'gallery.html'

    def get_context_data(self, **kwargs):
        context = super(GalleryView, self).get_context_data(**kwargs)

        context['albums'] = Album.objects.all()
        context['latest_news'] = News.objects.filter(is_posted=True)[:3]

        return context


class VideosView(TemplateView):
    template_name = 'videos.html'

    def get_context_data(self, **kwargs):
        context = super(VideosView, self).get_context_data(**kwargs)

        context['videos'] = Video.objects.all()
        context['latest_news'] = News.objects.filter(is_posted=True)[:3]

        return context


class VideoView(TemplateView):
    template_name = 'single_video.html'

    def get_context_data(self, **kwargs):
        context = super(VideoView, self).get_context_data(**kwargs)

        context['video'] = Video.objects.get(pk=kwargs['id'])
        context['latest_news'] = News.objects.filter(is_posted=True)[:3]

        return context


class AlbumView(TemplateView):
    template_name = 'album.html'

    def get_context_data(self, **kwargs):
        context = super(AlbumView, self).get_context_data(**kwargs)

        context['album'] = Album.objects.get(pk=kwargs['id'])
        context['pictures'] = Album.objects.get(pk=kwargs['id']).pictures.all()
        context['latest_news'] = News.objects.filter(is_posted=True)[:3]

        return context
