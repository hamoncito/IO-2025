import unittest

from entities.items.dvd import Dvd, Genre

class TestDvd(unittest.TestCase):
    def setUp(self):
        self.test_dvd = Dvd(
            id="1",
            title="Król lew",
            year=1994,
            director="Roger Allers",
            genre=Genre.ANIMATION,
            length_in_minutes=88
        )

        self.test_dvd_2_hours = Dvd(
            id="1",
            title="Król lew",
            year=1994,
            director="Roger Allers",
            genre=Genre.ANIMATION,
            length_in_minutes=135
        )

        self.test_dvd_less_than_hour = Dvd(
            id="1",
            title="Król lew",
            year=1994,
            director="Roger Allers",
            genre=Genre.ANIMATION,
            length_in_minutes=57
        )

    def test_get_creator(self):
        creator = self.test_dvd.get_creator()
        self.assertEqual(creator, "Roger Allers")

    def test_mark_unavailable(self):
        self.assertTrue(self.test_dvd.available)  # domyślnie jest dostępne

        self.test_dvd.mark_unavailable()

        self.assertFalse(self.test_dvd.available)  # dvd jest dostępne

    def test_mark_available(self):
        self.assertTrue(self.test_dvd.available) # domyślnie jest dostępne

        self.test_dvd.mark_unavailable()

        self.assertFalse(self.test_dvd.available) # dvd jest niedostępne

        self.test_dvd.mark_available()

        self.assertTrue(self.test_dvd.available) # dvd jest dostępne

    def test_get_genre(self):
        self.assertEqual(self.test_dvd.genre.value, "Animation")

    def test_show_movie_length(self):
        self.assertEqual(self.test_dvd.show_movie_length(), "Film trwa 1 godzinę i 28 min.")
        self.assertEqual(self.test_dvd_2_hours.show_movie_length(), "Film trwa 2 godziny i 15 min.")
        self.assertEqual(self.test_dvd_less_than_hour.show_movie_length(), "Film trwa 57 min.")
