from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView,
)
from django.db.models import Q

from core import models, forms


class ActorList(ListView):
    model = models.Actor
    template_name = 'core/actors.html'
    context_object_name = 'actors'

    def get_queryset(self):
        first_name = self.request.GET.get('first_name')
        second_name = self.request.GET.get('second_name')
        gender = self.request.GET.get('gender')
        qs = models.Actor.objects.all()
        query = Q()
        if first_name:
            query &= Q(first_name__icontains=first_name)
        if second_name:
            query &= Q(second_name__icontains=second_name)
        if gender:
            query &= Q(gender=gender)
        return qs.filter(query)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.ActorSearch(self.request.GET or None)
        return context


class ActorCreate(CreateView):
    model = models.Actor
    template_name = 'core/actor_create.html'
    form_class = forms.ActorForm
    success_url = reverse_lazy('core:actors')


class ActorUpdate(UpdateView):
    model = models.Actor
    template_name = 'core/actor_update.html'
    form_class = forms.ActorForm
    success_url = reverse_lazy('core:actors')


class ActorDelete(DeleteView):
    model = models.Actor
    template_name = 'core/actor_delete.html'
    success_url = reverse_lazy('core:actors')


class ActorDetail(DetailView):
    model = models.Actor
    template_name = 'core/actor_detail.html'
    context_object_name = 'actor'


class ActorIdList(ListView):
    model = models.ActorId
    template_name = 'core/actor_ids.html'
    context_object_name = 'actor_ids'


class PlayList(ListView):
    model = models.Play
    template_name = 'core/plays.html'
    context_object_name = 'plays'


class CreativeTeamList(ListView):
    model = models.CreativeTeam
    template_name = 'core/creative_teams.html'
    context_object_name = 'creative_teams'
