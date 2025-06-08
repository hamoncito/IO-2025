from __future__ import annotations
from typing import List

class Member:
    """
    Klasa reprezentująca członka biblioteki.

    Atrybuty:
        member_id (int): Unikalny identyfikator członka biblioteki.
        name (str): Imię członka.
        last_name (str): Nazwisko członka.
        email (str): Adres e-mail członka.
        rented_items (List[Rental]): Lista aktualnie wypożyczonych pozycji przez członka.

    Metody:
        get_overdue_rentals() -> List[Rental]:
            Zwraca listę wypożyczeń, które są przeterminowane według daty zwrotu.
    """
    def __init__(self,
                 member_id: int,
                 name: str,
                 last_name: str,
                 email: str,
                 rented_items: List["Rental"]
                 ):
        self.member_id = member_id
        self.name = name
        self.last_name = last_name
        self.email = email
        self.rented_items = rented_items

    def get_overdue_rentals(self) -> List["Rental"]:
        return [rental for rental in self.rented_items if rental.is_overdue()]
