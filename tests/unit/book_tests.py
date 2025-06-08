import unittest

from entities.items.book import Book


class TestBook(unittest.TestCase):
    def setUp(self):
        self.test_book = Book(
            id="1",
            title="Bracia Karmazow",
            year=1999,
            author="Fiodor Dostojewski",
        )

    def test_get_creator(self):
        creator = self.test_book.get_creator()
        self.assertEqual(creator, "Fiodor Dostojewski")

    def test_mark_unavailable(self):
        self.assertTrue(self.test_book.available)  # domyślnie jest dostępna

        self.test_book.mark_unavailable()

        self.assertFalse(self.test_book.available)  # książka jest niedostępna

    def test_mark_available(self):
        self.assertTrue(self.test_book.available) # domyślnie jest dostępna

        self.test_book.mark_unavailable()

        self.assertFalse(self.test_book.available) # książka jest niedostępna

        self.test_book.mark_available()

        self.assertTrue(self.test_book.available) # książka jest dostępna
