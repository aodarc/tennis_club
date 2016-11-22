from datetime import date

from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
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

        context['women'] = Member.objects.get_women().order_by('?')[:12]
        context['men'] = Member.objects.get_men().order_by('?')[:12]
        context['children'] = Member.objects.get_children().order_by('?')[:12]
        return context


class MembersRatingView(TemplateView):
    template_name = 'rating.html'

    def get_context_data(self, **kwargs):
        context = super(MembersRatingView, self).get_context_data(**kwargs)

        context['latest_news'] = News.objects.filter(is_posted=True)[:3]

        context['women'] = Member.objects.get_women().order_by('-rating')[:20]
        context['men'] = Member.objects.get_men().order_by('-rating')[:20]
        context['children'] = Member.objects.get_children().order_by('-rating')[:20]
        return context
