from django.conf.urls import url

from .views import GalleryView, AlbumView
urlpatterns = [
    url(r'^$', GalleryView.as_view(), name='gallery'),
    url(r'^album/(?P<id>[0-9]+)$', AlbumView.as_view(), name='album')
]
