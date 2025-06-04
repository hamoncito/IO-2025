from typing import List
from entities.rental import Rental

class Member:
    """
    Klasa reprezentująca członka biblioteki.

    Atrybuty:
        member_id (str): Unikalny identyfikator członka biblioteki.
        name (str): Imię członka.
        last_name (str): Nazwisko członka.
        email (str): Adres e-mail członka.
        rented_items (List[Rental]): Lista aktualnie wypożyczonych pozycji.

    Metody:
        borrow_item(Rental):
            Dodaje nowe wypożyczenie do listy wypożyczonych pozycji.

        return_item(Rental):
            Usuwa wypożyczenie z listy wypożyczonych pozycji.

        get_overdue_rentals():
            Zwraca listę wypożyczeń, które są przeterminowane.
    """
    def __init__(self,
                 member_id: str,
                 name: str,
                 last_name: str,
                 email: str,
                 rented_items: List[Rental]
                 ):
        self.member_id = member_id
        self.name = name
        self.last_name = last_name
        self.email = email
        self.rented_items = rented_items

    def borrow_item(self, rental: Rental):
        self.rented_items.append(rental)

    def return_item(self, rental: Rental):
        self.rented_items.remove(rental)

    #Modyfikacja oryginalnego get_borrowed_items()
    def get_overdue_rentals(self) -> List[Rental]:
        return [rental for rental in self.rented_items if rental.is_overdue()]
