from datetime import date, datetime

"""
    Klasa, która reprezentuje wypożyczenie przedmiotów (książek, magazynów czy DVD) dla pewnych użytkowników.
    
    Atrybuty:
        item (Item): Klasa przedmiotu dostępnego do wypożyczenia
        member (Member): Klasa wskazująca na osobę która chce wypożyczyć przedmiot
        rent_date (date): Atrybut daty wypożyczenia przedmiotu
        return_date (date): Atrybut daty zwrócenia przedmiotu
        returned (bool) = False: Zmienna wskazująca na zwrot przedmiotu
        
    Metody:
        is_overdue() -> Boolean:
            Sprawdza czy dane wypożyczenie przekroczyło czas możliwego wypożyczenia
        mark_returned() -> None:
            Metoda, która zwraca informacje, że wskazany przedmiot jest dostępny (Został zwrócony)
        calculate_return_date(daily_fine_for_overdue_items: Float = 2.0) -> Float:
            Kalkulacja, pozwalająca na ustalenie kary pieniężnej, w przypadku przedmiotu zwróconego za późno.
"""

class Rental:
    def __init__(self, item, member, rent_date: date, return_date: date):
        self.item = item
        self.member = member
        self.rent_date = rent_date
        self.return_date = return_date
        self.returned = False

    def is_overdue(self) -> bool:
        if self.returned:
            return False
        else:
            return datetime.now() > self.return_date

    def mark_returned(self) -> None:
        self.returned = True
        self.item.mark_available()

    def calculate_overdue_charge(self, daily_fine_for_overdue_items = 2.0) -> float:
        if not self.is_overdue():
            return 0.0
        else:
            days_over = (datetime.now() - self.return_date).days
            return days_over * daily_fine_for_overdue_items