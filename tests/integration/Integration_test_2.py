import pytest
from datetime import datetime, timedelta
from entities.items.book import Book
from entities.member import Member
from entities.rental import Rental
from entities.library import Library

"""
    Zwrot przeterminowanej pozycji
"""

def test_return_book_with_overdue_charge():
    book = Book(id=2, title="Lalka", year=1890, author="Bolesław Prus")
    member = Member(member_id=2, name="Anna", last_name="Nowak", email="anna@wp.pl", rented_items=[])

    rental = Rental(
        item=book,
        member=member,
        rent_date=datetime.now() - timedelta(days=40),
        return_date=datetime.now() - timedelta(days=10),
    )
    member.rented_items.append(rental)
    library = Library(items=[book], members=[member], rentals=[rental])

    library.remove_rental(rental, member)

    assert rental.returned
    assert book.available
    assert rental not in member.rented_items
    assert rental not in library.rentals