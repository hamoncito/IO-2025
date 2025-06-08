from entities.item import Item
from entities.member import Member
from datetime import date


"""
    Klasa, która reprezentuje wypożyczenie przedmiotów (książek, magazynów czy DVD) dla pewnych użytkowników.
    
    Atrybuty:
        item (Item): Klasa przedmiotu dostępnego do wypożyczenia
        member (Member): Klasa wskazująca na osobę która chce wypożyczyć przedmiot
        rent_date (date): Atrybut daty wypożyczenia przedmiotu
        return_date (date): Atrybut daty zwrócenia przedmiotu
        returned (bool) = False: Zmienna wskazująca na zwrot przedmiotu
        
    Metody:
        is_overdue():
            Sprawdza czy dane wypożyczenie przekroczyło czas możliwego wypożyczenia
        mark_returned():
            Metoda, która zwraca informacje, że wskazany przedmiot jest dostępny (Został zwrócony)
        calculate_return_date():
            Kalkulacja, pozwalająca na ustalenie kary pieniężnej, w przypadku przedmiotu zwróconego za późno.
"""

class Rental:
    def __init__(self, item: Item, member: Member, rent_date: date, return_date: date, returned: bool = False):
        self.item = item
        self.member = member
        self.rent_date = rent_date
        self.return_date = return_date
        self.returned = returned

    def is_overdue(self) -> bool:
        if self.returned:
            return False
        else:
            return date.today() > self.return_date

    def mark_returned(self):
        self.returned = True
        self.item.mark_available()

    def calculate_overdue_charge(self, daily_fine_for_overdue_items) -> float:
        if not self.is_overdue():
            return 0.0
        else:
            days_over = (date.today() - self.return_date).days
            return days_over * daily_fine_for_overdue_items