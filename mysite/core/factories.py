import factory
from faker import Factory

from core import models

factory_en = Factory.create(locale='en_US')


class CreativeTeamFactory(factory.django.DjangoModelFactory):
    name = factory_en.word()

    class Meta:
        model = models.CreativeTeam


class PlayFactory(factory.django.DjangoModelFactory):
    title = factory_en.word()
    premiere_date = factory_en.date()

    class Meta:
        model = models.Play


class ActorIdFactory(factory.django.DjangoModelFactory):
    number = str(factory_en.random_int(min=115, max=150))
    photo = factory_en.word()

    class Meta:
        model = models.ActorId


class ActorFactory(factory.django.DjangoModelFactory):
    first_name = factory_en.first_name()
    second_name = factory_en.last_name()
    gender = 'M'
    actorid = factory.SubFactory(ActorIdFactory)
    creativeteam = factory.SubFactory(CreativeTeamFactory)

    @factory.post_generation
    def plays(self, create, extracted):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of related models was passed in, add them.
            for play in extracted:
                self.plays.add(play)

    class Meta:
        model = models.Actor
