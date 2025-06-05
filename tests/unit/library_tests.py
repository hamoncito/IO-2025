import unittest
from entities.library import Library
from entities.item import Item
from entities.member import Member
from entities.rental import Rental

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.book1 = Item(id="1", title="Wiedźmin", year=1990, creator="Sapkowski")
        self.book2 = Item(id="2", title="Dziady", year=1832, creator="Mickiewicz")
        self.member1 = Member(
            member_id="1",
            name="Adam",
            last_name="Mickiewicz",
            email="adam@example.com",
            rented_items=[]
        )

        self.member2 = Member(
            member_id="2",
            name="Juliusz",
            last_name="Słowacki",
            email="juliusz@example.com",
            rented_items=[]
        )
        self.rental1 = Rental(is_overdue=False)
        self.rental2 = Rental(is_overdue=True)

        self.library = Library(
            items=[self.book1, self.book2],
            members=[self.member1],
            rentals=[self.rental1, self.rental2],
            daily_fine_for_overdue_items=2.0
        )

    def test_add_member(self):
        self.library.add_member(self.member2)
        self.assertIn(self.member2, self.library.get_all_members())

    def test_add_item(self):
        new_book = Item("Lalka")
        self.library.add_item(new_book)
        self.assertIn(new_book, self.library.get_all_items())

    def test_get_all_items(self):
        items = self.library.get_all_items()
        self.assertEqual(len(items), 2)

    def test_get_all_available_items(self):
        available = self.library.get_all_avalible_items()  # literówka w nazwie!
        self.assertEqual(len(available), 1)
        self.assertEqual(available[0].title, "Wiedźmin")

    def test_get_all_rentals(self):
        rentals = self.library.get_all_rentals()
        self.assertEqual(len(rentals), 2)

    def test_get_overdue_rentals(self):
        overdue = self.library.get_overdue_rentals()
        self.assertEqual(len(overdue), 1)
        self.assertTrue(overdue[0].is_overdue())

    def test_get_all_members(self):
        members = self.library.get_all_members()
        self.assertEqual(len(members), 1)
        self.assertEqual(members[0].name, "Adam Mickiewicz")