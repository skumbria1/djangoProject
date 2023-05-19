from django.contrib import admin

from core import models


@admin.register(models.Actor)
class Actor(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'second_name',
        'gender',
        'actorid',
        'creativeteam'
    )
    ordering = ('id',)


@admin.register(models.ActorId)
class ActorId(admin.ModelAdmin):
    list_display = ('number', 'photo',)
    ordering = ('number',)


@admin.register(models.CreativeTeam)
class CreativeTeam(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('id',)


@admin.register(models.Play)
class Play(admin.ModelAdmin):
    list_display = ('id', 'title', 'premiere_date')
    ordering = ('id',)
