from typing import List
from entities.item import Item
from entities.member import Member
from entities.rental import Rental

class Library:
    """
        A class to represent a library with items, members, and rentals.

        Attributes:
            items (List[Item]): List of all items in the library.
            members (List[Member]): List of all registered members.
            rentals (List[Rental]): List of current and past rentals.
            daily_fine_for_overdue_items (float): Daily fine applied to overdue items.

        Methods:
            add_member(member: Member) -> None:
                Adds a new member to the library.

            add_item(item: Item) -> None:
                Adds a new item to the library's collection.

            get_all_items() -> List[Item]:
                Returns a list of all items in the library.

            get_all_available_items() -> List[Item]:
                Returns a list of items that are currently available for rental.

            get_all_rentals() -> List[Rental]:
                Returns a list of all rental records.

            get_overdue_rentals() -> List[Rental]:
                Returns a list of rentals that are currently overdue.

            get_all_members() -> List[Member]:
                Returns a list of all registered members.
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

    def get_all_items(self) -> List[Item]:
        return self.items

    def get_all_avalible_items(self) -> List[Item]:
        return [item for item in self.items if item.avaliable]

    def get_all_rentals(self) -> List[Rental]:
        return self.rentals

    def get_overdue_rentals(self) -> List[Rental]:
        return [rental for rental in self.rentals if rental.is_overdue()]

    def get_all_members(self) -> List[Member]:
        return self.members