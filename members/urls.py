from django.conf.urls import url
from django.views.generic import TemplateView

from .views import PlayerView, MembersView

urlpatterns = [
    url(r'^$', MembersView.as_view(), name='players'),
    url(r'^player/(?P<pk>[0-9]+)$', PlayerView.as_view(), name='player')
]
