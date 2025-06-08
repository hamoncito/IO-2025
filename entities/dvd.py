from entities.item import Item
from enum import Enum

"""
   Klasa dziedzicząca po klasie Item (pozycja) reprezentująca płytę DVD.

   Atrybuty:
       id (str): Identyfikator płyty DVD.
       title (str): Rok produkcji filmu.
       year (int): Rok wydania płyty DVD.
       director (str): Reżyser filmu.
       genre (Genre): Gatunek filmu.

   Metody:
       get_creator() -> str:
           Zwraca reżysera filmu.
        
       def get_genre(self) -> str:
            Zwraca gatunek filmu.
   """

class Genre(Enum):
    ACTION = "Action",
    COMEDY = "Comedy",
    THRILLER= "Thriller",
    HORROR = "Horror",
    SCIENCE_FICTION= "Science Fiction",
    DOCUMENTARY = "Documentary",
    ROMANCE = "Romance",
    ANIMATION = "Animation"

class Dvd(Item):
    def __init__(self, id: str, title: str, year: int, director: str, genre: Genre):
        super().__init__(id, title, year)
        self.director = director
        self.genre = genre

    def get_creator(self) -> str:
        return self.director
