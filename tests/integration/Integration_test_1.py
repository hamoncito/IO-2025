import pytest
from entities.items.book import Book
from entities.member import Member
from entities.library import Library

"""
    Dodanie członka, pozycji i wypożyczenie książki
"""

def test_add_and_rent_book():
    book = Book(id=1, title="Wiedźmin", year=1990, author="Andrzej Sapkowski")
    member = Member(member_id=1, name="Jan", last_name="Kowalski", email="jan@wp.pl", rented_items=[])
    library = Library()

    library.add_item(book)
    library.add_member(member)
    library.add_rental(book, member)

    assert len(library.rentals) == 1
    assert not book.available
    assert member.rented_items[0].item == book