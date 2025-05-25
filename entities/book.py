from entities.item import Item

class Book(Item):
    def __init__(self, id: str, title: str, year: int, author: str):
        super().__init__(id, title, year)
        self.author = author

    def get_creator(self) -> str:
        return self.author