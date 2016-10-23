from django.conf.urls import url
from django.views.generic import TemplateView
from .views import NewsListView, NewsDetailView

urlpatterns = [
    url(r'^$', NewsListView.as_view(), name='news_list'),
    url(r'^(?P<slug>[-\w]+)/$', NewsDetailView.as_view(), name='news_post'),
]
