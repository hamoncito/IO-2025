import unittest
from datetime import datetime, timedelta
from entities.items.book import Book
from entities.member import Member
from entities.rental import Rental
from entities.library import Library


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.book1 = Book(id=1, title="Book A", year=2020, author="Author A")
        self.book2 = Book(id=2, title="Book B", year=2021, author="Author B")

        self.member1 = Member(
            member_id=101,
            name="Jan",
            last_name="Kowalski",
            email="jan.kowalski@example.com",
            rented_items=[]
        )

        self.library = Library(
            items=[self.book1, self.book2],
            members=[self.member1],
            rentals=[],
            daily_fine_for_overdue_items=2.0
        )

    def test_add_member(self):
        member2 = Member(102, "Anna", "Nowak", "anna.nowak@example.com", [])
        self.library.add_member(member2)
        self.assertIn(member2, self.library.members)

    def test_add_item(self):
        book3 = Book(id=3, title="Book C", year=2022, author="Author C")
        self.library.add_item(book3)
        self.assertIn(book3, self.library.items)

    def test_add_rental(self):
        self.library.add_rental(self.book1, self.member1)
        self.assertFalse(self.book1.available)
        self.assertEqual(len(self.library.rentals), 1)
        self.assertEqual(len(self.member1.rented_items), 1)
        rental = self.library.rentals[0]
        self.assertEqual(rental.item, self.book1)

    def test_remove_rental(self):
        self.library.add_rental(self.book1, self.member1)
        rental = self.library.rentals[0]
        self.library.remove_rental(rental, self.member1)
        self.assertTrue(rental.returned)
        self.assertNotIn(rental, self.library.rentals)
        self.assertNotIn(rental, self.member1.rented_items)
        self.assertTrue(self.book1.available)

    def test_get_all_available_items(self):
        self.library.add_rental(self.book1, self.member1)
        available_items = self.library.get_all_available_items()
        self.assertIn(self.book2, available_items)
        self.assertNotIn(self.book1, available_items)

    def test_get_all_rented_items(self):
        self.library.add_rental(self.book1, self.member1)
        rented_items = self.library.get_all_rented_items()
        self.assertIn(self.book1, rented_items)
        self.assertNotIn(self.book2, rented_items)

    def test_get_overdue_rentals(self):
        overdue_rental = Rental(
            item=self.book1,
            member=self.member1,
            rent_date=datetime.now() - timedelta(days=40),
            return_date=datetime.now() - timedelta(days=10)
        )
        self.member1.rented_items.append(overdue_rental)
        self.library.rentals.append(overdue_rental)

        overdue = self.library.get_overdue_rentals()
        self.assertIn(overdue_rental, overdue)

    def test_get_all_members_with_overdue(self):
        overdue_rental = Rental(
            item=self.book1,
            member=self.member1,
            rent_date=datetime.now() - timedelta(days=40),
            return_date=datetime.now() - timedelta(days=10)
        )
        self.member1.rented_items.append(overdue_rental)
        self.library.rentals.append(overdue_rental)

        overdue_members = self.library.get_all_members_with_overdue()
        self.assertIn(self.member1, overdue_members)