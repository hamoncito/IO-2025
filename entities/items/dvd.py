from entities.item import Item
from enum import Enum


class Genre(Enum):
    """
    Klasa enumertor (wyliczająca) z gatunkami filmów na DVD
    """

    ACTION = "Action"
    COMEDY = "Comedy"
    THRILLER = "Thriller"
    HORROR = "Horror"
    SCIENCE_FICTION = "Science Fiction"
    DOCUMENTARY = "Documentary"
    ROMANCE = "Romance"
    ANIMATION = "Animation"


class Dvd(Item):
    """
       Klasa dziedzicząca po klasie Item (pozycja) reprezentująca płytę DVD.

       Atrybuty:
           id (int): Identyfikator płyty DVD.
           title (str): Rok produkcji filmu.
           year (int): Rok wydania płyty DVD.
           director (str): Reżyser filmu.
           genre (Genre): Gatunek filmu.

       Metody:
           get_creator() -> str:
               Zwraca reżysera filmu.

           def show_movie_length(self) -> str:
                Zwraca czas filmu w godzinach i minutach
    """

    def __init__(self, id: int, title: str, year: int, director: str, genre: Genre, length_in_minutes: int):
        super().__init__(id, title, year)
        self.director = director
        self.genre = genre
        self.length_in_minutes = length_in_minutes

    def get_creator(self) -> str:
        return self.director

    def show_movie_length(self) -> str:
        hours = int(self.length_in_minutes / 60)
        minutes = self.length_in_minutes - hours * 60

        if hours == 1:
            return f"Film trwa {hours} godzinę i {minutes} min."
        if hours in (2, 3, 4):
            return f"Film trwa {hours} godziny i {minutes} min."
        else:
            return f"Film trwa {minutes} min."
