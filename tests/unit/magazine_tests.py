import unittest

from entities.magazine import Magazine


class TestMagazine(unittest.TestCase):
    def setUp(self):
        self.test_magazine = Magazine(
            id="1",
            title="Życie na gorąco",
            year=1999,
            author="Tomasz Szymański",
        )

    def test_get_creator(self):
        creator = self.test_magazine.get_creator()
        self.assertEqual(creator, "Tomasz Szymański")

    def test_mark_unavailable(self):
        self.assertTrue(self.test_magazine.available)  # domyślnie jest dostępny

        self.test_magazine.mark_unavailable()

        self.assertFalse(self.test_magazine.available)  # magazyn jest niedostępny

    def test_mark_available(self):
        self.assertTrue(self.test_magazine.available) # domyślnie jest dostępna

        self.test_magazine.mark_unavailable()

        self.assertFalse(self.test_magazine.available) # magazyn jest niedostępny

        self.test_magazine.mark_available()

        self.assertTrue(self.test_magazine.available) # magazyn jest dostępny
