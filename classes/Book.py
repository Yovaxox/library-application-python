import random


class Book:
    ids = set()
    rand = random.Random()

    def __init__(self, name, author):
        while True:
            self.id = Book.rand.randint(0, 999)
            if self.id not in Book.ids:
                Book.ids.add(self.id)
                break

        self.name = name
        self.author = author
        self.is_rented = False

    # Getters
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_author(self):
        return self.author

    def get_is_rented(self):
        return self.is_rented

    # Setters
    def set_name(self, name):
        self.name = name

    def set_author(self, author):
        self.author = author

    def set_is_rented(self, is_rented):
        self.is_rented = is_rented
