class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Library:
    def __init__(self):
        self.head = None
        
    def insert_beginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

        print("Book inserted at beginning.")

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            print("Book inserted at end.")
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

        print("Book inserted at end.")

    def delete_beginning(self):
        if self.head is None:
            print("Library catalog is empty.")
            return

        deleted = self.head.data
        self.head = self.head.next

        print("Book deleted:", deleted)

    def display(self):
        if self.head is None:
            print("Library catalog is empty.")
            return

        temp = self.head

        print("\nLibrary Catalog:")
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

library = Library()

while True:
    print("\n===== DYNAMIC LIBRARY CATALOG =====")
    print("1. Insert at beginning")
    print("2. Insert at end")
    print("3. Delete from beginning")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        library.insert_beginning(book)

    elif choice == 2:
        book = input("Enter book name: ")
        library.insert_end(book)

    elif choice == 3:
        library.delete_beginning()

    elif choice == 4:
        library.display()

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice.")
