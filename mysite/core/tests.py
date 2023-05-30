from django.test import TestCase, Client
from django.urls import reverse

from core import factories, models


class ActorTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.plays = factories.PlayFactory.create_batch(3)
        self.actor = factories.ActorFactory.create(plays=self.plays)

    def test_actor_list_is_reachable(self):
        response = self.client.get(reverse('core:actors'))
        self.assertEqual(response.status_code, 200)

    def test_actor_detail_is_reachable(self):
        response = self.client.get(reverse(
            'core:actor_detail', kwargs={'pk': self.actor.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_actor_id_list_is_reachable(self):
        response = self.client.get(reverse('core:actor_ids'))
        self.assertEqual(response.status_code, 200)

    def test_play_list_is_reachable(self):
        response = self.client.get(reverse('core:plays'))
        self.assertEqual(response.status_code, 200)

    def test_creative_team_list_is_reachable(self):
        response = self.client.get(reverse('core:creative_teams'))
        self.assertEqual(response.status_code, 200)

    def test_actor_create(self):
        data = {
            'first_name': self.actor.first_name,
            'second_name': self.actor.second_name,
            'gender': self.actor.gender,
            'actorid': self.actor.actorid,
            'creativeteam': self.actor.creativeteam,
            'plays': self.plays,
        }
        response = self.client.post(
            path=reverse('core:actor_create'), data=data, follow=True,
        )
        self.assertEqual(response.status_code, 200)
        retrieved_actor = models.Actor.objects.first()
        self.assertListEqual(
            [
                self.actor.first_name,
                self.actor.second_name,
                self.actor.gender,
                self.actor.actorid.number,
                self.actor.actorid.photo,
                self.actor.creativeteam.name,
                [play.title for play in self.plays],
                [play.premiere_date for play in self.plays],
            ],
            [
                retrieved_actor.first_name,
                retrieved_actor.second_name,
                retrieved_actor.gender,
                retrieved_actor.actorid.number,
                retrieved_actor.actorid.photo,
                retrieved_actor.creativeteam.name,
                [play.title for play in retrieved_actor.plays.all()],
                [
                    play.premiere_date.strftime('%Y-%m-%d')
                    for play in retrieved_actor.plays.all()
                ],
            ]
        )

    def test_actor_update(self):
        data = {
            'first_name': self.actor.first_name + 'upd',
            'second_name': self.actor.second_name + 'upd',
            'gender': 'F',
        }
        response = self.client.post(
            path=reverse('core:actor_update', args=(self.actor.pk,)),
            data=data,
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        retrieved_actor = models.Actor.objects.first()
        self.assertListEqual(
            [
                self.actor.first_name + 'upd',
                self.actor.second_name + 'upd',
                'F',
            ],
            [
                retrieved_actor.first_name,
                retrieved_actor.second_name,
                retrieved_actor.gender,
            ]
        )

    def test_actor_delete(self):
        response = self.client.post(
            reverse('core:actor_delete', args=(self.actor.pk,)), follow=True,
        )
        self.assertEqual(response.status_code, 200)
        retrieved_actor = models.Actor.objects.first()
        self.assertEqual(retrieved_actor, None)
