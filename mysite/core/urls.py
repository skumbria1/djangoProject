"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from . import views


app_name = 'core'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/actors/')),
    path('actors/', views.ActorList.as_view(), name='actors'),
    path('actors_f/', views.get_actor_list, name='actors_f'),
    path(
        'actor_detail/<int:pk>',
        views.ActorDetail.as_view(),
        name='actor_detail'
    ),
    path(
        'actor_detail_f/<int:pk>',
        views.get_actor_detail,
        name='actor_detail_f'
    ),
    path('actor_ids/', views.ActorIdList.as_view(), name='actor_ids'),
    path('actor_ids_f/', views.get_actor_id_list, name='actor_ids_f'),
    path(
        'creative_teams/',
        views.CreativeTeamList.as_view(),
        name='creative_teams'
    ),
    path(
        'creative_teams_f/',
        views.get_creative_team_list,
        name='creative_teams_f'
    ),
    path('plays/', views.PlayList.as_view(), name='plays'),
    path('plays_f/', views.get_play_list, name='plays_f'),
]
