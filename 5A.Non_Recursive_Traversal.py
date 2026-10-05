class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


def inorder(root):
    stack = Stack()
    current = root

    while current is not None or not stack.is_empty():

        while current is not None:
            stack.push(current)
            current = current.left

        current = stack.pop()
        print(current.data, end=" ")

        current = current.right


def preorder(root):
    if root is None:
        return

    stack = Stack()
    stack.push(root)

    while not stack.is_empty():

        current = stack.pop()
        print(current.data, end=" ")

        # Push right first
        if current.right is not None:
            stack.push(current.right)

        # Push left second
        if current.left is not None:
            stack.push(current.left)


root = None

n = int(input("Enter number of nodes: "))

for i in range(n):
    data = int(input("Enter data: "))
    root = insert(root, data)

print("\nInorder Traversal:")
inorder(root)

print("\nPreorder Traversal:")
preorder(root)
