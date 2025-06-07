from enum import member
from typing import List
from collections import Counter
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
        daily_fine_for_overdue_items (float): Dzienna kara naliczana za przetrzymane pozycje.

    Metody:
        add_member(member: Member) -> None:
            Dodaje nowego członka do biblioteki.

        add_item(item: Item) -> None:
            Dodaje nową pozycję do zbiorów biblioteki.

        get_all_available_items() -> List[Item]:
            Zwraca listę pozycji aktualnie dostępnych do wypożyczenia.

        get_most_popular_creator() -> str:
            Zwraca nazwę twórcy (np. autora), którego pozycje są najczęściej wypożyczane (niedostępne).

        get_all_member_rented_from_library(member: Member) -> List[Rental]:
            Zwraca listę wypożyczeń powiązanych z podanym członkiem biblioteki.

        get_overdue_rentals() -> List[Rental]:
            Zwraca listę wypożyczeń, które są przeterminowane.

        get_all_members_with_overdue() -> List[Member]:
            Zwraca listę członków biblioteki, którzy mają przeterminowane wypożyczenia.
    """

    def __init__(
            self,
            items: List[Item],
            members: List[Member],
            rentals: List[Rental],
            daily_fine_for_overdue_items: float
    ):
        self.items = items
        self.members = members
        self.rentals = rentals
        self.daily_fine_for_overdue_items = daily_fine_for_overdue_items

    def add_member(self, Member):
        self.members.append(Member)

    def add_item(self, Item):
        self.items.append(Item)

    def get_most_popular_creator(self) -> str:
        creator_list = []
        for item in self.items:
            if not item.avaliable:
                creator_list.append(item.get_creator())
        counter = Counter(creator_list)
        return counter.most_common(1)[0][0]

    def get_all_avalible_items(self) -> List[Item]:
        return [item for item in self.items if item.avaliable]

    def get_all_member_rented_from_library(self, member: Member) -> List[Rental]:
        return [rental for rental in self.rentals if rental.member == member]

    def get_overdue_rentals(self) -> List[Rental]:
        return [rental for rental in self.rentals if rental.is_overdue()]

    def get_all_members_with_overdue(self) -> List[Member]:
        members_list = []
        for member in self.members:
            for rental in member.rented_items():
                if rental.is_overdue():
                    members_list.append(member)
        return members_list
