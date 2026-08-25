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
    if root is not None:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)
        
def Inorder(root):
    if root is not None:
        preorder(root.left)
        print(root.data,end=" ")
        preorder(root.right)
    
def Postorder(root):
    if root is not None:
        preorder(root.left)
        preorder(root.right)
        print(root.data,end=" ")
 
root = create()

print("Postorder")
Postorder(root)

print("\nPreorder")
preorder(root)

print("\nInorder")
Inorder(root)
