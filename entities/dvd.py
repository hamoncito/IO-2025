from entities.item import Item

class Dvd(Item):
    def __init__(self, id: str, title: str, year: int, director: str, genre: str):
        super().__init__(id, title, year, director)
        self.genre = genre

    def get_creator(self) -> str:
        return self.creator

    def get_genre(self) -> str:
        return self.genre