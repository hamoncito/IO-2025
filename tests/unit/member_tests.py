import unittest
from datetime import datetime, timedelta
from entities.item import Item
from entities.member import Member
from entities.rental import Rental


class TestMember(unittest.TestCase):
    def setUp(self):
        self.item1 = Item(id="1", title="Wiedźmin", year=1990, creator="Sapkowski")
        self.item2 = Item(id="2", title="Dziady", year=1832, creator="Mickiewicz")

        self.member = Member(
            member_id="001",
            name="Adam",
            last_name="Mickiewicz",
            email="adam@example.com",
            rented_items=[]
        )

        # Przeterminowane wypożyczenie (ręcznie dodane do listy)
        self.overdue_rental = Rental(
            item=self.item2,
            member=self.member,
            rent_date=datetime.now() - timedelta(days=40),
            return_date=datetime.now() - timedelta(days=10),
            returned=False
        )

    def test_borrow_item(self):
        self.member.borrow_item(self.item1)
        self.assertEqual(len(self.member.rented_items), 1)
        rental = self.member.rented_items[0]
        self.assertEqual(rental.item.title, "Wiedźmin")
        self.assertEqual(rental.member.name, "Adam")

    def test_borrow_unavailable_item(self):
        self.item1.available = False
        self.member.borrow_item(self.item1)
        self.assertEqual(len(self.member.rented_items), 0)

    def test_return_item(self):
        self.member.borrow_item(self.item1)
        rental = self.member.rented_items[0]

        self.member.return_item(rental)

        self.assertTrue(rental.returned)
        self.assertTrue(self.item1.available)
        self.assertEqual(len(self.member.rented_items), 0)

    def test_get_overdue_rentals(self):
        self.member.rented_items.append(self.overdue_rental)
        overdue = self.member.get_overdue_rentals()
        self.assertEqual(len(overdue), 1)
        self.assertTrue(overdue[0].is_overdue())