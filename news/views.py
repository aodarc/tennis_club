from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import News

# Create your views here.


class NewsListView(ListView):
    template_name = 'news_list.html'
    model = News
    context_object_name = 'news_list'

    def get_context_data(self, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)
        context['now'] = ''
        return context


class NewsDetailView(DetailView):
    model = News
    template_name = 'single_news.html'
    context_object_name = 'news_object'

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        return context