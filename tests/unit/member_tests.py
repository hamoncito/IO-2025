import unittest
from datetime import datetime, timedelta
from entities.book import Book
from entities.member import Member
from entities.rental import Rental


class TestMember(unittest.TestCase):
    def setUp(self):
        self.book1 = Book(id="1", title="Wiedźmin", year=1990, author="Sapkowski")
        self.book2 = Book(id="2", title="Dziady", year=1832, author="Mickiewicz")

        self.member = Member(
            member_id="001",
            name="Adam",
            last_name="Mickiewicz",
            email="adam@example.com",
            rented_items=[]
        )

        self.overdue_rental = Rental(
            item=self.book2,
            member=self.member,
            rent_date=datetime.now() - timedelta(days=40),
            return_date=datetime.now() - timedelta(days=10),
            returned=False
        )

    def test_borrow_item(self):
        new_book = Book(id="3", title="Lalka", year=1890, author="Prus")
        self.member.borrow_item(new_book)
        self.assertEqual(len(self.member.rented_items), 3)
        self.assertFalse(new_book.available)

    def test_borrow_unavailable_item(self):
        self.book1.available = False
        self.member.borrow_item(self.book1)
        self.assertEqual(len(self.member.rented_items), 0)

    def test_return_item(self):
        self.member.borrow_item(self.book1)
        rental = self.member.rented_items[0]

        self.member.return_item(rental)

        self.assertTrue(rental.returned)
        self.assertTrue(self.book1.available)
        self.assertEqual(len(self.member.rented_items), 0)

    def test_get_overdue_rentals(self):
        self.member.rented_items.append(self.overdue_rental)
        overdue = self.member.get_overdue_rentals()
        self.assertEqual(len(overdue), 1)
        self.assertTrue(overdue[0].is_overdue())