class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append({"name": book, "issued": False})
        print(book, "added.")

    def remove_book(self, book):
        for b in self.books:
            if b["name"] == book:
                self.books.remove(b)
                print(book, "removed.")
                return
        print("Book not found.")

    def issue_book(self, book):
        for b in self.books:
            if b["name"] == book:
                if not b["issued"]:
                    b["issued"] = True
                    print(book, "issued.")
                else:
                    print("Book is already issued.")
                return
        print("Book not found.")

    def return_book(self, book):
        for b in self.books:
            if b["name"] == book:
                b["issued"] = False
                print(book, "returned.")
                return
        print("Book not found.")

    def display_books(self):
        print("\nBooks in Library:")
        for b in self.books:
            status = "Issued" if b["issued"] else "Available"
            print(b["name"], "-", status)


library = Library()

library.add_book("The Alchemist")
library.add_book("Wings of Fire")

library.display_books()

library.issue_book("The Alchemist")
library.display_books()

library.return_book("The Alchemist")
library.remove_book("Wings of Fire")

library.display_books()
