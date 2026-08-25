class Stack:
    def __init__(self):
        self.top = -1
        self.ST = [0] * 5

    def Insert(self, x):
        if self.top == 4:
            print("Stack is full")
        else:
            self.top += 1
            self.ST[self.top] = x
            print("Value inserted")

    def Delete(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            x = self.ST[self.top]
            self.top -= 1
            print("Deleted value:", x)

    def Display(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print("Stack elements:")
            for i in range(self.top, -1, -1):
                print(self.ST[i])


s1 = Stack()

while True:
    print("\n===== Call Stack =====")
    print("1. Insert value in stack")
    print("2. Delete Top value")
    print("3. Display stack")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        x = int(input("Enter value: "))
        s1.Insert(x)

    elif choice == 2:
        s1.Delete()

    elif choice == 3:
        s1.Display()

    elif choice == 4:
        print("Program ended.")
        break

    else:
        print("Invalid choice")
