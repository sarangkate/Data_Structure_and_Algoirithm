class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def create():
    n = int(input("Enter data to create node(0 to stop): "))
    if n == 0:
        return None
    root = Node(n)
    print((f"Enter left of {n}: "))
    root.left = create()
    print((f"Enter right of {n}: "))
    root.right = create()
    return root

class Stack:
    def __init__(self):
        self.top = -1
        self.ST = [0]*5

    def push(self,root):
        if self.top == 4:
            print("Stack is full")
        else:
            self.top += 1
            self.ST[self.top] = root

    def pop(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            x = self.ST[self.top]
            self.top = self.top - 1
            return x

def preorder(root):
    s = Stack()
    while root is not None:
        print(root.data)
        s.push(root)
        root = root.left
    while s.top != -1:
        root = s.pop()
        root = root.right
        while root is not None:
            print(root.data)
            s.push(root)
            root = root.left

def Inorder(root):
    s = Stack()
    while root is not None:
        s.push(root)
        root = root.left
    while s.top != -1:
        root = s.pop()
        print(root.data)
        root = root.right
        while root is not None:
            s.push(root)
            root = root.left
    
def Postorder(root):
    s1 = Stack()
    s2 = Stack()
    
    s1.push(root)
    while s1.top != -1:
        current  = s1.pop()
        s2.push(current)
        if current.left is not None:
            s1.push(current.left)
        if current.right is not None:
            s1.push(current.right)
    while s2.top != -1:
        node = s2.pop()
        print(node.data)

root = create()

print("Postorder")
Postorder(root)

print("\nPreorder")
preorder(root)

print("\nInorder")
Inorder(root)
