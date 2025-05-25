from abc import ABC, abstractmethod

class Item(ABC):
    """
    Klasa abstrakcyjna, po której dziedziczą klasy Book, Magazine, DVD
    """
    def __init__(self, id: str, title: str, year: int):
        self.id = id
        self.title =  title
        self.year = year
        self.available = True # domyślnie pozycja jest dostępna

    @abstractmethod
    def get_creator(self) -> str:
        """
        Metoda abstrakcyjna, zwracająca twórcę pozycji (autora, reżysera, redaktora)
        """
        pass

    def mark_unavailable(self) -> None:
        """
        Metoda oznaczająca pozycję jako wypożyczoną
        """
        self.available = False

    def mark_available(self) -> None:
        """
        Metoda oznaczająca pozycję jako dostępną
        """
        self.available = True