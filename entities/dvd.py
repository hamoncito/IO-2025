from entities.item import Item

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

from enum import Enum
class Genre(Enum): ACTION = "Action" COMEDY = "Comedy" THRILLER= "Thriller" HORROR = "Horror" SCIENCE_FICTION= "Science Fiction" DOCUMENTARY = "Documentary" ROMANCE = "Romance"

class Dvd(Item): def init(self, id: str, title: str, year: int, director: str, genre: Genre): super().init(id, title, year, director) self.genre = genre

def get_creator(self) -> str:
    return self.creator

def get_genre(self) -> str:
    return self.genre