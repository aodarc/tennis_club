from django.conf.urls import url

from .views import GalleryView, AlbumView, VideosView, VideoView
urlpatterns = [
    url(r'^$', GalleryView.as_view(), name='gallery'),
    url(r'^videos$', VideosView.as_view(), name='videos'),
    url(r'^videos/(?P<id>[0-9]+)$', VideoView.as_view(), name='video'),
    url(r'^album/(?P<id>[0-9]+)$', AlbumView.as_view(), name='album')
]
