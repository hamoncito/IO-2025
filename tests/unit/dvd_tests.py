import unittest

from entities.dvd import Dvd, Genre

class TestDvd(unittest.TestCase):
    def setUp(self):
        self.test_dvd = Dvd(
            id="1",
            title="Król lew",
            year=1994,
            director="Roger Allers",
            genre=Genre.ANIMATION
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
