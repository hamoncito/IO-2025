import pytest
from datetime import datetime, timedelta
from entities.items.book import Book
from entities.member import Member
from entities.rental import Rental
from entities.library import Library
"""
Pobranie listy członków z przeterminowanymi wypożyczeniami
"""

def test_get_all_members_with_overdue():
    book1 = Book(id=3, title="Pan Tadeusz", year=1834, author="Adam Mickiewicz")
    book2 = Book(id=4, title="Krzyżacy", year=1900, author="Henryk Sienkiewicz")

    member1 = Member(member_id=3, name="Tomek", last_name="Jakiś", email="tomek@wp.pl", rented_items=[])
    member2 = Member(member_id=4, name="Ala", last_name="Jakaśinna", email="ala@wp.pl", rented_items=[])

    overdue_rental = Rental(
        item=book1,
        member=member1,
        rent_date=datetime.now() - timedelta(days=50),
        return_date=datetime.now() - timedelta(days=20),
    )
    not_overdue_rental = Rental(
        item=book2,
        member=member2,
        rent_date=datetime.now(),
        return_date=datetime.now() + timedelta(days=10),
    )

    member1.rented_items.append(overdue_rental)
    member2.rented_items.append(not_overdue_rental)

    library = Library(items=[book1, book2], members=[member1, member2], rentals=[overdue_rental, not_overdue_rental])

    overdue_members = library.get_all_members_with_overdue()

    assert len(overdue_members) == 1
    assert overdue_members[0] == member1