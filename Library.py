class Book:
    def __init__(self, title, author, status):
        self.title = title
        self.author = author
        self.status = status

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author, "Available"))

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"{title} removed from library.")
                return
        print(f"{title} not found in library.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.status == "Available":
                book.status = "Borrowed"
                print(f"{title} borrowed successfully.")
                return
        print(f"{title} not available or not found in library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.status == "Borrowed":
                book.status = "Available"
                print(f"{title} returned successfully.")
                return
        print(f"{title} not borrowed or not found in library.")

    def display_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Status: {book.status}")

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Display Books")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)
        elif choice == "2":
            title = input("Enter book title: ")
            library.remove_book(title)
        elif choice == "3":
            title = input("Enter book title: ")
            library.borrow_book(title)
        elif choice == "4":
            title = input("Enter book title: ")
            library.return_book(title)
        elif choice == "5":
            library.display_books()
        elif choice == "6":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()

