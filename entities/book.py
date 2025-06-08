from entities.item import Item

"""
   Klasa dziedzicząca po klasie Item (pozycja) reprezentująca książkę.

   Atrybuty:
       id (int): Identyfikator książki.
       title (str): Tytuł książki.
       year (int): Rok wydania książki.
       author (str): Autor książki.

   Metody:
       get_creator() -> str:
           Zwraca autora książki.
   """
class Book(Item):
    def __init__(self, id: int, title: str, year: int, author: str):
        super().__init__(id, title, year)
        self.author = author

    def get_creator(self) -> str:
        return self.author
