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
from django.urls import path
from django.views.generic import RedirectView

from core import views

app_name = 'core'

urlpatterns = [
    path('', RedirectView.as_view(url='/actors/')),
    path('actors/', views.ActorList.as_view(), name='actors'),
    path(
        'actor_detail/<int:pk>',
        views.ActorDetail.as_view(),
        name='actor_detail'
    ),
    path('actor_ids/', views.ActorIdList.as_view(), name='actor_ids'),
    path(
        'creative_teams/',
        views.CreativeTeamList.as_view(),
        name='creative_teams'
    ),
    path('plays/', views.PlayList.as_view(), name='plays'),
    path('actor_create/', views.ActorCreate.as_view(), name='actor_create'),
    path(
        'actor_update/<int:pk>',
        views.ActorUpdate.as_view(),
        name='actor_update'
    ),
    path(
        'actor_delete/<int:pk>',
        views.ActorDelete.as_view(),
        name='actor_delete'
    ),
]
