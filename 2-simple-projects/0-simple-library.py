class Library:

    def __init__(self, book_list):
        self.available_books = book_list

    def display_available_book(self):
        print("Available books: ")
        for book in self.available_books:
            print(book)

    def lend_book(self, requested_book):
        if requested_book in self.available_books:
            print("You have now borrowed the book")
            self.available_books.remove(requested_book)
        else:
            print("Sorry, the book is already taken")

    def add_book(self, returned_book):
        self.available_books.append(returned_book)
        print("Book returned successfully")


class Customer:
    def request_book(self):
        print("Name of the book to borrow: ")
        self.book_name = input()
        return self.book_name

    def return_book(self):
        print("Name of the book to return :")
        self.book_name = input()
        return self.book_name


library = Library(['Book One', 'Book Two', 'Book Three'])

customer = Customer()

while True:
    print("Enter 1 to display available books: ")
    print("Enter 2 to request for a book: ")
    print("Enter 3 to return a book: ")
    print("Enter 4 to exit")

    user_choice = int(input())
    if user_choice == 1:
        library.display_available_book()
    elif user_choice == 2:
        requested_book = customer.request_book()
        library.lend_book(requested_book)
    elif user_choice == 3:
        return_book = customer.return_book()
        library.add_book(return_book)
    elif user_choice == 4:
        quit()
