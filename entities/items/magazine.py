from entities.item import Item


class Magazine(Item):
    """
       Klasa dziedzicząca po klasie Item (pozycja) reprezentująca magazyn.

       Atrybuty:
           id (int): Identyfikator magazynu.
           title (str): Tytuł magazynu.
           year (int): Rok wydania magazynu.
           editor (str): Redaktor magazynu.

       Metody:
           get_creator() -> str:
               Zwraca redaktora magazynu.
    """
    def __init__(self, id: int, title: str, year: int, editor: str):
        super().__init__(id, title, year)
        self.editor = editor

    def get_creator(self) -> str:
        return self.editor
