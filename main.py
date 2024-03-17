from classes.User import User
from classes.Book import Book
import os

# Create an array list to store the users
users = []
# Create an array list to store the books
books = []


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_first_menu_option():
    # Print the first menu
    print("-----------------------------------------------")
    print("| 1. Register new user                        |")
    print("| 2. Register new book                        |")
    print("| 3. Register new book rental                 |")
    print("| 4. List all registered users                |")
    print("| 5. List all registered books                |")
    print("| 6. List all users who have rented one book  |")
    print("| 7. List all books that have NOT been rented |")
    print("| 8. List all books that have been rented     |")
    print("| 9. Exit the application                     |")
    print("-----------------------------------------------")

    # Get the user's input
    menu_option = int(input("Please, select an option: "))
    clear_screen()
    return menu_option


def register_new_user():
    try:
        print("---------------------")
        print("| Register new user |")
        print("---------------------")

        # Get the user's name
        user_name = input("\nPlease, enter the user's name: ")
        while not user_name.strip():
            clear_screen()
            print("\033[0;31m" + "User's name cannot be empty. Please try again." + "\033[0m")
            user_name = input("Please, enter the user's name: ")

        # Get the user's age
        while True:
            try:
                age = int(input("Please, enter the user's age: "))
                if age > 0:
                    break
                else:
                    clear_screen()
                    print("\033[0;31m" + "User's age cannot be negative or zero. Please try again." + "\033[0m")
            except ValueError:
                clear_screen()
                print("\033[0;31m" + "Invalid input. Please enter a number." + "\033[0m")

        clear_screen()

        # Create a new user
        users.append(User(user_name, age))
        print("\033[0;32m" + "User registered successfully." + "\033[0m")
    except Exception as e:
        print("\033[0;31m" + "An error occurred: " + str(e) + "\033[0m")


def register_new_book():
    try:
        print("---------------------")
        print("| Register new book |")
        print("---------------------")

        # Get the book's title
        book_title = input("Please, enter the book's title: ")
        while not book_title.strip():
            clear_screen()
            print("\033[0;31m" + "Book's title cannot be empty. Please try again." + "\033[0m")
            book_title = input("Please, enter the book's title: ")

        # Get the book's author
        book_author = input("Please, enter the book's author: ")
        while not book_author.strip():
            clear_screen()
            print("\033[0;31m" + "Book's author cannot be empty. Please try again." + "\033[0m")
            book_author = input("Please, enter the book's author: ")

        clear_screen()

        # Create a new book
        books.append(Book(book_title, book_author))
        print("\033[0;32m" + "Book registered successfully." + "\033[0m")
    except Exception as e:
        print("\033[0;31m" + "An error occurred: " + str(e) + "\033[0m")


def register_new_book_rental():
    try:
        if not users:
            print("\033[0;31m" + "There are no registered users. Please, register a new user first." + "\033[0m")
            return
        elif not books:
            print("\033[0;31m" + "There are no registered books. Please, register a new book first." + "\033[0m")
            return

        print("----------------------------")
        print("| Register new book rental |")
        print("----------------------------")

        # Get the user's ID
        user_id = 0
        while True:
            try:
                # Display all users
                print("\nList of all registered users")
                print("-----------------------------")
                for user in users:
                    print("ID: " + str(user.get_id()) + " | Name: " + user.get_name() + " | Age: " + str(user.get_age()))

                user_id = int(input("\nPlease enter the user's ID to rent a book. Check the list above: "))

                # Check if the user's ID is valid
                user_exists = False
                for user in users:
                    if user.get_id() == user_id:
                        user_exists = True
                        break

                if not user_exists:
                    clear_screen()
                    print("\033[0;31m" + "User's ID does not exist. Please try again." + "\033[0m")
                    continue
                else:
                    clear_screen()
                    break

            except ValueError:
                clear_screen()
                print("\033[0;31m" + "Invalid input. Please enter a number." + "\033[0m")

        print("----------------------------")
        print("| Register new book rental |")
        print("----------------------------")

        # Get the book's ID
        book_id = 0
        while True:
            try:
                # Display all unrented books
                print("\nList of all unrented books")
                print("-----------------------------")
                for book in books:
                    if not book.get_is_rented():
                        print("ID: " + str(book.get_id()) + " | Name: " + book.get_name() + " | Author: " + book.get_author())

                book_id = int(input("\nPlease enter the book's ID to be rented. Check the list above: "))

                # Check if the book's ID is valid and not rented
                book_exists = False
                for book in books:
                    if book.get_id() == book_id and not book.get_is_rented():
                        book_exists = True
                        break

                if not book_exists:
                    clear_screen()
                    print("\033[0;31m" + "Book's ID does not exist or it has already been rented. Please try again." + "\033[0m")
                    continue
                else:
                    clear_screen()
                    break

            except ValueError:
                clear_screen()
                print("\033[0;31m" + "Invalid input. Please enter a number." + "\033[0m")

        # Set the book as rented
        for book in books:
            if book.get_id() == book_id:
                book.set_is_rented(True)
                break

        # Set the rented book to the user
        for user in users:
            if user.get_id() == user_id:
                for book in books:
                    if book.get_id() == book_id:
                        user.get_rented_books().append(book)
                        break
                break

        print("\033[0;32m" + "Book rented successfully." + "\033[0m")
    except Exception as e:
        print("\033[0;31m" + "An error occurred: " + str(e) + "\033[0m")


def list_all_registered_users():
    try:
        if not users:
            print("\033[0;31m" + "There are no registered users." + "\033[0m")
            return

        print("------------------------")
        print("| List of all users    |")
        print("------------------------")

        for user in users:
            print("ID: " + str(user.get_id()) + " | Name: " + user.get_name() + " | Age: " + str(user.get_age()))

        input("\nPress Enter to continue...")
        clear_screen()
    except Exception as e:
        print("\033[0;31m" + "An error occurred: " + str(e) + "\033[0m")


def list_all_registered_books():
    try:
        if not books:
            print("\033[0;31m" + "There are no registered books." + "\033[0m")
            return

        print("------------------------")
        print("| List of all books    |")
        print("------------------------")

        for book in books:
            print("ID: " + str(book.get_id()) + " | Name: " + book.get_name() + " | Author: " + book.get_author())

        input("\nPress Enter to continue...")
        clear_screen()
    except Exception as e:
        print("\033[0;31m" + "An error occurred: " + str(e) + "\033[0m")


def list_all_users_have_rented():
    try:
        if not users:
            print("\033[0;31m" + "There are no registered users." + "\033[0m")
            return

        has_rented_books = False
        for user in users:
            if user.get_rented_books():
                has_rented_books = True
                break

        if not has_rented_books:
            print("\033[0;31m" + "There are no users who have rented a book." + "\033[0m")
            return

        print("----------------------------------------------")
        print("| List of all users who have rented one book |")
        print("----------------------------------------------\n")

        for user in users:
            if user.get_rented_books():
                print("----------------------------------------------")
                print("ID: " + str(user.get_id()) + " | Name: " + user.get_name() + " | Age: " + str(user.get_age()))
                print("\nRented books:")
                for book in user.get_rented_books():
                    print(
                        "ID: " + str(book.get_id()) + " | Name: " + book.get_name() + " | Author: " + book.get_author())
                print("----------------------------------------------\n")

        input("\nPress Enter to continue...")
        clear_screen()
    except Exception as e:
        print("\033[0;31m" + "An error occurred: " + str(e) + "\033[0m")


def list_all_books_not_rented():
    try:
        if not books:
            print("\033[0;31m" + "There are no registered books." + "\033[0m")
            return

        has_not_rented_books = False
        for book in books:
            if not book.get_is_rented():
                has_not_rented_books = True
                break

        if not has_not_rented_books:
            print("\033[0;31m" + "There are no books that have not been rented." + "\033[0m")
            return

        print("-----------------------------------------------")
        print("| List of all books that have NOT been rented |")
        print("-----------------------------------------------\n")

        for book in books:
            if not book.get_is_rented():
                print("ID: " + str(book.get_id()) + " | Name: " + book.get_name() + " | Author: " + book.get_author())

        input("\nPress Enter to continue...")
        clear_screen()
    except Exception as e:
        print("\033[0;31m" + "An error occurred: " + str(e) + "\033[0m")


def list_all_books_rented():
    try:
        if not books:
            print("\033[0;31m" + "There are no registered books." + "\033[0m")
            return

        has_rented_books = False
        for book in books:
            if book.get_is_rented():
                has_rented_books = True
                break

        if not has_rented_books:
            print("\033[0;31m" + "There are no books that have been rented." + "\033[0m")
            return

        print("----------------------------------------------")
        print("| List of all books that have been rented    |")
        print("----------------------------------------------\n")

        for book in books:
            if book.get_is_rented():
                print("ID: " + str(book.get_id()) + " | Name: " + book.get_name() + " | Author: " + book.get_author())

        input("\nPress Enter to continue...")
        clear_screen()
    except Exception as e:
        print("\033[0;31m" + "An error occurred: " + str(e) + "\033[0m")


if __name__ == "__main__":
    try:
        print("\033[H\033[2J")
        print("Welcome to the Library Application.")

        while True:
            menu_option = get_first_menu_option()

            if menu_option == 1:
                register_new_user()
            elif menu_option == 2:
                register_new_book()
            elif menu_option == 3:
                register_new_book_rental()
            elif menu_option == 4:
                list_all_registered_users()
            elif menu_option == 5:
                list_all_registered_books()
            elif menu_option == 6:
                list_all_users_have_rented()
            elif menu_option == 7:
                list_all_books_not_rented()
            elif menu_option == 8:
                list_all_books_rented()
            elif menu_option == 9:
                print("You have exited the application.")
                break
            else:
                clear_screen()
                print("\033[0;31m" + "Invalid option" + "\033[0m")
    except Exception as e:
        print("\033[0;31m" + "An error occurred: " + str(e) + "\033[0m")
