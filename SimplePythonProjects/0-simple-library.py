class Library:
    """A library class that performs books
    lending and management functionalities

    """

    def __init__(self, book_list):
        self.available_books = book_list

    def display_available_book(self):
        """Displays available books in the library"""
        for book in self.available_books:
            print("Available books: {} ".format(book))

    def lend_book(self, requested_book):
        """Shows books available for lending

        Checks if the requested book is in the collection
        if the book is available, lend the book to the user
        then remove the book for the list

        """
        if self.requested_book in self.available_book:
            print("You have now borrowed the book")
            self.available_books.remove(requested_book)
        else:
            print("Sorry, the book is not available in our list")

    def add_book(self, returned_book):
        """Adds return books to the library
        and update the count

        """
        self.available_books.append(returned_book)
        print("Book returned successfully")


class Customer:
    """Shows books available for lending

    """

    def request_book(self):
        """Allows a customer to enter a book ne he/she wants to
        borrow

        """
        print("Name of the book to borrow: ")
        self.book_name = input()
        return self.book_name

    def return_book(self, return_book_name):
        """once the customer returns the book,
        we add the book back to the list

        """
        print("Name of the book to return:{}".format(self.return_book_name))
        self.return_book_name = input()
        return self.return_book_name
        # print()


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
    elif  user_choice == 4:
        quit()
