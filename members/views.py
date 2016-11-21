from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from members.models import Member
from news.models import News


class PlayerView(DetailView):
    template_name = 'single_player.html'
    context_object_name = 'player'
    model = Member

    def get_context_data(self, **kwargs):
        context = super(PlayerView, self).get_context_data(**kwargs)

        context['latest_news'] = News.objects.filter(is_posted=True)[:3]

        return context


class MembersView(TemplateView):
    template_name = 'players.html'

    def get_context_data(self, **kwargs):
        context = super(MembersView, self).get_context_data(**kwargs)

        context['latest_news'] = News.objects.filter(is_posted=True)[:3]

        context['women'] = [m for m in Member.objects.filter(sex='f').order_by('?') if not m.is_child][:12]
        context['men'] = [m for m in Member.objects.filter(sex='m').order_by('?') if not m.is_child][:12]
        context['children'] = [m for m in Member.objects.order_by('?') if m.is_child][:12]

        print(context)
        return context
