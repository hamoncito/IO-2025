from __future__ import annotations
from datetime import datetime, timedelta
from typing import List
from entities.item import Item

class Member:
    """
    Klasa reprezentująca członka biblioteki.

    Atrybuty:
        member_id (int): Unikalny identyfikator członka biblioteki.
        name (str): Imię członka.
        last_name (str): Nazwisko członka.
        email (str): Adres e-mail członka.
        rented_items (List[Rental]): Lista aktualnie wypożyczonych pozycji.

    Metody:
        borrow_item(item: Item) -> None:
            Tworzy nowe wypożyczenie dla podanej pozycji z datą wypożyczenia od dziś i terminem zwrotu za 31 dni.
            Dodaje wypożyczenie do listy wypożyczonych pozycji.

        return_item(rental: Rental) -> None:
            Zwraca wypożyczoną pozycję. Jeśli wypożyczenie jest przeterminowane, oblicza opłatę
            i wyświetla komunikat o konieczności jej uiszczenia. Zaznacza pozycję jako zwróconą
            i usuwa ją z listy wypożyczonych pozycji.

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

    def borrow_item(self, item: Item) -> "Rental":
        from entities.rental import Rental
        if item.available:
            rental = Rental(
                item = item,
                member = self,
                rent_date = datetime.now(),
                return_date = datetime.now() + timedelta(days=31))
            self.rented_items.append(rental)
            item.available = False
            return rental
        else:
            raise NameError("Pozycja jest niedostępna")

    def return_item(self, rental: "Rental") -> None:
        if rental.returned:
            print("Pozycja została już zwrócona")
        else:
            if rental.is_overdue():
                charge = rental.calculate_overdue_charge()
                print(f"W związku z opóźnieniem członek biblioteki {self.name} {self.last_name} musi zapłacić {charge} zł!")
            rental.mark_returned()
            self.rented_items.remove(rental)

    def get_overdue_rentals(self) -> List["Rental"]:
        return [rental for rental in self.rented_items if rental.is_overdue()]
