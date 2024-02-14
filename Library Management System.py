class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def close_file(self):
        self.file.close()

    def list_books(self):
        print("*** LIST BOOKS ***")
        self.file.seek(0)
        file_content = self.file.read()        
        lines = file_content.splitlines()
        
        for line in lines:
            book_info = line.split(',')
            book_name = book_info[0]
            author = book_info[1]
            print("Book:", book_name)
            print("Author:", author, "\n")

            
    def add_book(self):
        print("*** ADD BOOK ***")
        title = input("Enter the title: ")
        author = input("Enter the author: ")
        release_year = input("Enter release year: ")
        num_pages = input("Enter number of pages: ")
        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully!\n")

    def remove_book(self):
        print("*** REMOVE BOOK ***")
        title = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        books = self.file.readlines()
        updated = []
        found = False
        for book in books:
            if title.lower() not in book.lower():
                updated.append(book)
            else:
                found = True
        if found:
            self.file.seek(0)
            self.file.truncate()
            self.file.writelines(updated)
            print("Book removed successfully!\n")
        else:
            print("Book not found!\n")


def main():
    lib = Library()
    choice = ""
    while choice != "q":

        print("*** MENU ***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        print("4) Quit")

        choice = input("Enter your choice (1/2/3/q): ")
        print()

        if choice == "1":
            lib.list_books()
        elif choice == "2":
            lib.add_book()
        elif choice == "3":
            lib.remove_book()
        elif choice == "q":
            lib.close_file()
        else:
            print("Invalid choice! Please enter 1, 2, 3, or q.\n")

if __name__ == "__main__":
    main()

