from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from . import models


class ActorList(ListView):
    model = models.Actor
    template_name = 'core/actors.html'
    context_object_name = 'actors'


def get_actor_list(request):
    actors = models.Actor.objects.all()
    context = {'actors': actors}
    return render(
        request=request,
        template_name='core/actors.html',
        context=context
    )


class ActorDetail(DetailView):
    model = models.Actor
    template_name = 'core/actor_detail.html'
    context_object_name = 'actor'


def get_actor_detail(request, pk):
    actor = get_object_or_404(models.Actor, pk=pk)
    context = {'actor': actor}
    return render(
        request=request,
        template_name='core/actor_detail.html',
        context=context
    )


class ActorIdList(ListView):
    model = models.ActorId
    template_name = 'core/actor_ids.html'
    context_object_name = 'actor_ids'


def get_actor_id_list(request):
    actor_ids = models.ActorId.objects.all()
    context = {'actor_ids': actor_ids}
    return render(
        request=request,
        template_name='core/actor_ids.html',
        context=context
    )


class PlayList(ListView):
    model = models.Play
    template_name = 'core/plays.html'
    context_object_name = 'plays'


def get_play_list(request):
    plays = models.Play.objects.all()
    context = {'plays': plays}
    return render(
        request=request,
        template_name='core/plays.html',
        context=context
    )


class CreativeTeamList(ListView):
    model = models.CreativeTeam
    template_name = 'core/creative_teams.html'
    context_object_name = 'creative_teams'


def get_creative_team_list(request):
    creative_teams = models.CreativeTeam.objects.all()
    context = {'creative_teams': creative_teams}
    return render(
        request=request,
        template_name='core/creative_teams.html',
        context=context
    )
