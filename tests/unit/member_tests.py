import unittest
from datetime import timedelta, datetime
from entities.book import Book
from entities.member import Member
from entities.rental import Rental


class TestMember(unittest.TestCase):
    def setUp(self):
        self.book1 = Book(id="1", title="Wiedźmin", year=1990, author="Sapkowski")
        self.book2 = Book(id="2", title="Lalka", year=1890, author="Bolesław Prus")

        self.member = Member(
            member_id="001",
            name="Adam",
            last_name="Mickiewicz",
            email="adam@example.com",
            rented_items=[]
        )

        self.overdue_rental = Rental(
            item = self.book1,
            member = self.member,
            rent_date = datetime.now() - timedelta(days=40),
            return_date = datetime.now() - timedelta(days=10),
        )
        self.book1.mark_unavailable()

        # Aktualne wypożyczenie
        self.valid_rental = Rental(
            item = self.book2,
            member = self.member,
            rent_date = datetime.now() - timedelta(days=5),
            return_date = datetime.now() + timedelta(days=10),
        )
        self.book2.mark_unavailable()

        self.member.rented_items.extend([self.overdue_rental, self.valid_rental])

    def test_get_overdue_rentals(self):
        overdue = self.member.get_overdue_rentals()
        self.assertIn(self.overdue_rental, overdue)
        self.assertNotIn(self.valid_rental, overdue)
