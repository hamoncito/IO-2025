import unittest
from datetime import datetime, timedelta
from entities.item import Item
from entities.member import Member
from entities.rental import Rental
from entities.library import Library


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.book1 = Item(id="1", title="Wiedźmin", year=1990, creator="Sapkowski")
        self.book2 = Item(id="2", title="Dziady", year=1832, creator="Mickiewicz")
        self.book3 = Item(id="3", title="Narrenturm", year=2000, creator="Sapkowski")

        self.member1 = Member("1", "Adam", "Mickiewicz", "adam@pw.edu.pl", [])
        self.member2 = Member("2", "Juliusz", "Słowacki", "julek@pw.edu.pl", [])

        self.rental1 = Rental(
            item=self.book1,
            member=self.member1,
            rent_date=datetime.now() - timedelta(days=20),
            return_date=datetime.now() - timedelta(days=5),
        )
        self.book1.mark_unavailable()
        self.member1.rented_items.append(self.rental1)

        self.rental2 = Rental(
            item=self.book3,
            member=self.member2,
            rent_date=datetime.now() - timedelta(days=5),
            return_date=datetime.now() + timedelta(days=10),
        )
        self.book3.mark_unavailable()
        self.member2.rented_items.append(self.rental2)

        self.library = Library(
            items=[self.book1, self.book2, self.book3],
            members=[self.member1, self.member2],
            rentals=[self.rental1, self.rental2],
            daily_fine_for_overdue_items=2.0,
        )

    def test_get_most_popular_creator(self):
        self.assertEqual(self.library.get_most_popular_creator(), "Sapkowski")

    def test_get_all_member_rented_from_library(self):
        rentals = self.library.get_all_member_rented_from_library(self.member1)
        self.assertEqual(rentals, [self.rental1])

    def test_get_overdue_rentals(self):
        overdue = self.library.get_overdue_rentals()
        self.assertIn(self.rental1, overdue)
        self.assertNotIn(self.rental2, overdue)

    def test_get_all_members_with_overdue(self):
        members_with_overdue = self.library.get_all_members_with_overdue()
        self.assertIn(self.member1, members_with_overdue)
        self.assertNotIn(self.member2, members_with_overdue)

    def test_get_all_available_items(self):
        available_items = self.library.get_all_available_items()
        self.assertEqual(len(available_items), 1)
        self.assertEqual(available_items[0], self.book2)