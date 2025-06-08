from abc import ABC, abstractmethod


class Item(ABC):
    """
    Klasa abstrakcyjna reprezentująca pozycję w bibliotece, z której dziedziczą konkretne typy pozycji (Book, Magazine, DVD).

    Atrybuty:
        id (str): Identyfikator pozycji.
        title (str): Tytuł pozycji.
        year (int): Rok wydania pozycji.
        available (bool) = True: Dostępność pozycji

    Metody:
        get_creator() -> str:
            Metoda abstrakcyjna, zwracająca twórcę pozycji (autora, reżysera, redaktora).
        mark_unavailable() -> None:
            Oznacza pozycję jako wypożyczoną (niedostępną).
        mark_available() -> None:
            Oznacza pozycję jako dostępną.
    """

    def __init__(self, id: int, title: str, year: int):
        self.id = id
        self.title = title
        self.year = year
        self.available = True

    @abstractmethod
    def get_creator(self) -> str:
        pass

    def mark_unavailable(self) -> None:
        self.available = False

    def mark_available(self) -> None:
        self.available = True
