import random


class User:
    ids = set()
    rand = random.Random()

    def __init__(self, name, age):
        while True:
            self.id = User.rand.randint(0, 999)
            if self.id not in User.ids:
                User.ids.add(self.id)
                break

        self.name = name
        self.age = age
        self.rented_books = []

    # Getters
    def get_id(self):
        return self.id

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def get_rented_books(self):
        return self.rented_books

    # Setters
    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name

    def set_rented_books(self, rented_books):
        self.rented_books = rented_books

    # Methods
