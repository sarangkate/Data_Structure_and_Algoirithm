class Library:
    def __init__(self):
        self.top = -1
        self.books = [None] * 5

    def ReturnBook(self, book):
        if self.top == 4:
            print("Return stack is full")
        else:
            self.top += 1
            self.books[self.top] = book
            print("Book returned successfully")

    def ProcessReturn(self):
        if self.top == -1:
            print("No books to process")
        else:
            book = self.books[self.top]
            self.top -= 1
            print("Book processed:", book)

    def Display(self):
        if self.top == -1:
            print("No returned books")
        else:
            print("Returned books:")
            for i in range(self.top, -1, -1):
                print(self.books[i])


library = Library()

while True:
    print("\n===== Library Book Return Management =====")
    print("1. Return a book")
    print("2. Process latest returned book")
    print("3. Display returned books")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        library.ReturnBook(book)

    elif choice == 2:
        library.ProcessReturn()

    elif choice == 3:
        library.Display()

    elif choice == 4:
        print("Program ended.")
        break

    else:
        print("Invalid choice")
