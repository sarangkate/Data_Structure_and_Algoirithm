class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def create(self):
        n = int(input("Enter no. of nodes: "))
        if n <= 0:
            print("Enter valid no. of nodes: ")
            return
        for i in range(1,n+1):
            val = input(f"Enter data for node {i}: ")
            self.insert(val)
    def insert(self,val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return 
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
    def show(self):
        if self.head == None:
            print("Nothing to print...")
            return
        temp = self.head
        while temp is not None:
            print(temp.data,end="->")
            temp = temp.next
    def delete(self,dlt):
        if self.head == None:
            print("Linked list is empty.")
            return

        if self.head.data == dlt:
            self.head = self.head.next
            print("Node deleted")
            return

        prev = self.head
        temp = self.head.next

        while temp is not None:
            if temp.data == dlt:
                prev.next = temp.next
                print("Node deleted")
                return
            prev = temp
            temp = temp.next

        print("Node not found.")
        
        

s1 = Linked_list()
while True:
    print("\n1.Create Linked list")
    print("2.Show")
    print("3.Exit")
    print("4.Delete")

    choice = int(input("Enter choice: "))

    if choice == 1:
        s1.create()
    if choice == 2:
        s1.show()
    if choice == 3:
        break
    if choice == 4:
        dlt = input("Enter data: ")
        s1.delete(dlt)
        
    
        
