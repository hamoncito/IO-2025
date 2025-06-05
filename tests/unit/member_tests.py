import unittest
from entities.member import Member
from entities.rental import Rental


class TestMember(unittest.TestCase):
    def setUp(self):
        self.rental_not_overdue = Rental(is_overdue=False)
        self.rental_overdue = Rental(is_overdue=True)

        self.member = Member(
            member_id="001",
            name="Adam",
            last_name="Mickiewicz",
            email="adam@example.com",
            rented_items=[self.rental_not_overdue]
        )

    def test_borrow_item(self):
        self.member.borrow_item(self.rental_overdue)
        self.assertIn(self.rental_overdue, self.member.rented_items)
        self.assertEqual(len(self.member.rented_items), 2)

    def test_return_item(self):
        self.member.borrow_item(self.rental_overdue)
        self.member.return_item(self.rental_overdue)
        self.assertNotIn(self.rental_overdue, self.member.rented_items)
        self.assertEqual(len(self.member.rented_items), 1)

    def test_get_overdue_rentals(self):
        self.member.borrow_item(self.rental_overdue)
        overdue = self.member.get_overdue_rentals()
        self.assertIn(self.rental_overdue, overdue)
        self.assertNotIn(self.rental_not_overdue, overdue)
        self.assertEqual(len(overdue), 1)