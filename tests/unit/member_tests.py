import unittest
from datetime import date, timedelta
from entities.book import Book
from entities.member import Member
from entities.rental import Rental


class TestMember(unittest.TestCase):
    def setUp(self):
        # Przygotowanie pozycji książkowych
        self.book1 = Book(id="1", title="Wiedźmin", year=1990, author="Sapkowski")
        self.book2 = Book(id="2", title="Lalka", year=1890, author="Bolesław Prus")

        # Przygotowanie członka
        self.member = Member(
            member_id="001",
            name="Adam",
            last_name="Mickiewicz",
            email="adam@example.com",
            rented_items=[]
        )

        # Przeterminowane wypożyczenie
        self.overdue_rental = Rental(
            item=self.book1,
            member=self.member,
            rent_date=date.today() - timedelta(days=40),
            return_date=date.today() - timedelta(days=10),
            returned=False
        )
        self.book1.mark_unavailable()

        # Aktualne wypożyczenie
        self.valid_rental = Rental(
            item=self.book2,
            member=self.member,
            rent_date=date.today() - timedelta(days=5),
            return_date=date.today() + timedelta(days=10),
            returned=False
        )
        self.book2.mark_unavailable()

        self.member.rented_items.extend([self.overdue_rental, self.valid_rental])

    def test_borrow_item(self):
        new_book = Book(id="3", title="Dziady", year=1822, author="Adam Mickiewicz")
        self.member.borrow_item(new_book)
        self.assertFalse(new_book.available)

    def test_return_item(self):
        self.member.return_item(self.valid_rental)
        self.assertTrue(self.valid_rental.returned)
        self.assertTrue(self.valid_rental.item.available)
        self.assertNotIn(self.valid_rental, self.member.rented_items)

    def test_get_overdue_rentals(self):
        overdue = self.member.get_overdue_rentals()
        self.assertIn(self.overdue_rental, overdue)
        self.assertNotIn(self.valid_rental, overdue)

    def test_get_overdue_rentals_empty_after_returned(self):
        self.member.return_item(self.overdue_rental)
        overdue = self.member.get_overdue_rentals()
        self.assertEqual(overdue, [])