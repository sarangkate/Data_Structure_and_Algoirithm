class TicketCounter:
    def __init__(self):
        self.front = -1
        self.rear = -1
        self.QT = [0] * 5

    def AddCustomer(self, name):
        if self.rear == 4:
            print("Queue is full")
        else:
            self.rear += 1
            self.QT[self.rear] = name

            if self.front == -1:
                self.front = 0

            print("Customer added to queue")

    def ServeCustomer(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            name = self.QT[self.front]

            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front += 1

            return name

    def Display(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            print("Customers waiting in queue:")
            for i in range(self.front, self.rear + 1):
                print(self.QT[i])


counter = TicketCounter()

while True:
    print("\n===== Ticket Booking Counter =====")
    print("1. Add customer to queue")
    print("2. Serve customer")
    print("3. Display waiting customers")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter customer name: ")
        counter.AddCustomer(name)

    elif choice == 2:
        name = counter.ServeCustomer()

        if name is not None:
            print("Ticket booked for:", name)

    elif choice == 3:
        counter.Display()

    elif choice == 4:
        print("Program ended.")
        break

    else:
        print("Invalid choice")
