class Queue:
    def __init__(self):
        self.front = -1
        self.rear = -1
        self.QT = [0] * 5

    def Insert(self, x):
        if self.rear == 4:
            print("Queue is full")
        else:
            self.rear += 1
            self.QT[self.rear] = x

            if self.front == -1:
                self.front = 0

            print("Value inserted")

    def Delete(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            x = self.QT[self.front]

            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front += 1

            return x

    def Display(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            print("Queue elements:")
            for i in range(self.front, self.rear + 1):
                print(self.QT[i])


s1 = Queue()

while True:
    print("\n===== Queue =====")
    print("1. Insert value in queue")
    print("2. Delete front value")
    print("3. Display queue")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        x = int(input("Enter value: "))
        s1.Insert(x)

    elif choice == 2:
        x = s1.Delete()

        if x is not None:
            print("Deleted value:", x)

    elif choice == 3:
        s1.Display()

    elif choice == 4:
        print("Program ended.")
        break

    else:
        print("Invalid choice")
