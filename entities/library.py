from typing import List
from entities.item import Item
from entities.member import Member
from entities.rental import Rental


class Library:
    """
    Klasa reprezentująca bibliotekę zawierającą pozycje, członków i wypożyczenia.

    Atrybuty:
        items (List[Item]): Lista wszystkich pozycji znajdujących się w bibliotece.
        members (List[Member]): Lista wszystkich zarejestrowanych członków.
        rentals (List[Rental]): Lista bieżących i przeszłych wypożyczeń.
        daily_fine_for_overdue_items (float) = 2.0: Dzienna kara naliczana za przetrzymane pozycje.

    Metody:
        add_member(member: Member) -> None:
            Dodaje nowego członka do biblioteki.

        add_item(item: Item) -> None:
            Dodaje nową pozycję do zbiorów biblioteki.

        add_rental(rental: Rental) -> None:
            Dodaje nowe wypożyczenie do biblioteki.

        get_all_available_items() -> List[Item]:
            Zwraca listę pozycji aktualnie dostępnych do wypożyczenia.

        get_overdue_rentals() -> List[Rental]:
            Zwraca listę wypożyczeń, które są przeterminowane.

        get_all_members_with_overdue() -> List[Member]:
            Zwraca listę członków biblioteki, którzy mają przeterminowane wypożyczenia.

        get_all_members_with_overdue() -> List[Member]:
            Zwraca listę członków biblioteki, którzy mają przeterminowane wypożyczenia.
    """

    def __init__(
            self,
            items: List[Item] = [],
            members: List[Member] = [],
            rentals: List[Rental] = [],
            daily_fine_for_overdue_items: float = 2.0
    ):
        self.items = items
        self.members = members
        self.rentals = rentals
        self.daily_fine_for_overdue_items = daily_fine_for_overdue_items

    def add_member(self, member) -> None:
        self.members.append(member)

    def add_item(self, item) -> None:
        self.items.append(item)

    def add_rental(self, rental) -> None:
        self.rentals.append(rental)

    def get_all_available_items(self) -> List[Item]:
        return [item for item in self.items if item.available]

    def get_overdue_rentals(self) -> List[Rental]:
        return [rental for rental in self.rentals if rental.is_overdue()]

    def get_all_members_with_overdue(self) -> List[Member]:
        members_list = []
        for member in self.members:
            for rental in member.rented_items:
                if rental.is_overdue():
                    members_list.append(member)
        return members_list

    def get_all_rented_items(self) -> List[Item]:
        rented_items = []
        for rental in self.rentals:
            rented_items.append(rental.item)
        return rented_items
