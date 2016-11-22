from django.conf.urls import url
from django.views.generic import TemplateView

from .views import PlayerView, MembersView, MembersRatingView

urlpatterns = [
    url(r'^$', MembersView.as_view(), name='players'),
    url(r'^rating$', MembersRatingView.as_view(), name='rating'),
    url(r'^player/(?P<pk>[0-9]+)$', PlayerView.as_view(), name='player')
]
