# import unittest
import datetime
from django.test import TestCase, Client
from .models import Movie

# Create your tests here.

# Testing the Movie Model
class MovieTestCase(TestCase):
    def setUp(self):
        Movie.objects.create(
            title="Independence Day",
            released_date="1996-03-10",
            production_company="Centropolis Entertainment"
        )

    def test_movies_exist(self):
        movie = Movie.objects.get(title="Independence Day")
        self.assertEqual(movie.title, "Independence Day")
        self.assertEqual(movie.released_date, datetime.date(1996, 3, 10))
        self.assertEqual(movie.production_company, "Centropolis Entertainment")


# Testing the views
class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_movies_index(self):
        response = self.client.get('/api/v1/movies')
        self.assertEqual(response.status_code, 200)

    def test_movies_detail_with_no_content(self):
        response = self.client.get('/api/v1/movies/1')
        self.assertEqual(response.status_code, 404)

    def test_movies_detail_with_content(self):
        movie = Movie.objects.create(
            title="Armageddon",
            released_date="1998-07-01",
            production_company="Touchstone Pictures"
        )
        url = '/api/v1/movies/' + str(movie.id)
        # import pdb; pdb.set_trace()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)