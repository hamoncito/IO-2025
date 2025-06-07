from entities.item import Item

"""
   Klasa dziedzicząca po klasie Item (pozycja) reprezentująca magazyn.

   Atrybuty:
       id (str): Identyfikator magazynu.
       title (str): Tytuł magazynu.
       year (int): Rok wydania magazynu.
       editor (str): Redaktor magazynu.

   Metody:
       get_creator() -> str:
           Zwraca redaktora magazynu.
   """
class Magazine(Item):
    def __init__(self, id: str, title: str, year: int, editor: str):
        super().__init__(id, title, year, editor)

    def get_creator(self) -> str:
        return self.creator
