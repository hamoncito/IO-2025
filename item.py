from abc import ABC, abstractmethod

class Item(ABC):
    """
    Klasa abstrakcyjna, po której dziedziczą klasy Book, Magazine, DVD
    """
    def __init__(self, id: str, title: str, year: int, creator: str):
        self.id = id
        self.title =  title
        self.year = year
        self.creator = creator
        self.available = True # domyślnie pozycja jest dostępna

    def get_creator(self) -> str:
        return self.creator

    def mark_unavailable(self) -> None:
        self.available = False

    def mark_available(self) -> None:
        self.available = True