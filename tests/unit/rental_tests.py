import unittest
from datetime import date, timedelta
from unittest.mock import Mock
from entities.rental import Rental  # Zakładamy, że klasa Rental jest w pliku rental.py


class TestRental(unittest.TestCase):
    def setUp(self):
        # Mock obiektów Item i Member
        self.mock_item = Mock()
        self.mock_member = Mock()

        # Dzisiejsza data
        self.today = date.today()
        self.past_date = self.today - timedelta(days=5)
        self.future_date = self.today + timedelta(days=5)

    def test_is_overdue_false_when_not_returned_and_due_in_future(self):
        rental = Rental(self.mock_item, self.mock_member, self.today, self.future_date)
        self.assertFalse(rental.is_overdue())

    def test_is_overdue_true_when_not_returned_and_due_in_past(self):
        rental = Rental(self.mock_item, self.mock_member, self.today, self.past_date)
        self.assertTrue(rental.is_overdue())

    def test_is_overdue_false_when_already_returned(self):
        rental = Rental(self.mock_item, self.mock_member, self.today, self.past_date)
        rental.returned = True
        self.assertFalse(rental.is_overdue())

    def test_mark_returned_sets_returned_to_true_and_marks_item_available(self):
        rental = Rental(self.mock_item, self.mock_member, self.today, self.future_date)
        rental.mark_returned()
        self.assertTrue(rental.returned)
        self.mock_item.mark_available.assert_called_once()

    def test_calculate_overdue_charge_zero_when_not_overdue(self):
        rental = Rental(self.mock_item, self.mock_member, self.today, self.future_date)
        fine = rental.calculate_overdue_charge(daily_fine_for_overdue_items=2.0)
        self.assertEqual(fine, 0.0)

    def test_calculate_overdue_charge_correct_when_overdue(self):
        rental = Rental(self.mock_item, self.mock_member, self.today, self.past_date)
        daily_fine = 1.5
        expected_days = (self.today - self.past_date).days
        expected_fine = expected_days * daily_fine
        self.assertAlmostEqual(rental.calculate_overdue_charge(daily_fine), expected_fine)

    def test_calculate_overdue_charge_zero_if_returned(self):
        rental = Rental(self.mock_item, self.mock_member, self.today, self.past_date)
        rental.mark_returned()
        fine = rental.calculate_overdue_charge(daily_fine_for_overdue_items=2.0)
        self.assertEqual(fine, 0.0)


if __name__ == "__main__":
    unittest.main()
