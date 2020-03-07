from django.test import TestCase
from django.contrib.auth.models import User
from games.models import Game


class GameListViewTests(TestCase):
    def test_multiple_games(self):
        user = User.objects.create()

        Game.objects.create(title="Yakuza", price="14")
        Game.objects.create(title="Test Game", price="17")

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

    
        responses = response.context['games']
        self.assertEqual(len(responses), 2)

        self.assertQuerysetEqual(
            responses,
            ['<Game: Yakuza>', '<Game: Test Game>'],
            ordered=False
        )

class GameListTests(TestCase):
    def test_list(self):
    
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_uploadgame(self):
        
        response = self.client.get('/new-game')
        self.assertEqual(response.status_code, 301)


class AnimalTestCase(TestCase):
    def setUp(self):
        Game.objects.create(title="test", price="10")
        Game.objects.create(title="test2", price="13")

    def test_games(self):
        test = Game.objects.get(title="test")
        test2 = Game.objects.get(title="test2")
    