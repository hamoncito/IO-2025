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
        daily_fine_for_overdue_items (float): Dzienna kara naliczana za przetrzymane pozycje.

    Metody:
        add_member(member: Member) -> None:
            Dodaje nowego członka do biblioteki.

        add_item(item: Item) -> None:
            Dodaje nową pozycję do zbiorów biblioteki.

        get_all_items() -> List[Item]:
            Zwraca listę wszystkich pozycji w bibliotece.

        get_all_available_items() -> List[Item]:
            Zwraca listę pozycji aktualnie dostępnych do wypożyczenia.

        get_all_rentals() -> List[Rental]:
            Zwraca listę wszystkich rekordów wypożyczeń.

        get_overdue_rentals() -> List[Rental]:
            Zwraca listę wypożyczeń, które są przeterminowane.

        get_all_members() -> List[Member]:
            Zwraca listę wszystkich zarejestrowanych członków.
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

    def add_member(self, member) -> None:
        self.members.append(member)

    def add_item(self, item) -> None:
        self.items.append(item)

    def get_all_items(self) -> List[Item]:
        return self.items

    def get_all_available_items(self) -> List[Item]:
        return [item for item in self.items if item.available]

    def get_all_rentals(self) -> List[Rental]:
        return self.rentals

    def get_overdue_rentals(self) -> List[Rental]:
        return [rental for rental in self.rentals if rental.is_overdue()]

    def get_all_members(self) -> List[Member]:
        return self.members