from classes import User, Book


class Library:
    def __init__(self, users, books):
        self.users = users.copy() if users else []
        self.books = books.copy() if books else []

    # Getters
    def get_users(self):
        return self.users

    def get_books(self):
        return self.books

    # Setters
    def set_users(self, users):
        self.users = users

    def set_books(self, books):
        self.books = books

    # Methods
    def show_users(self):
        for user in self.users:
            print(user)
