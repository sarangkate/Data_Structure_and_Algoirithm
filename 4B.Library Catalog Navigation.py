class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create():
    data = input("Enter book name (0 to stop): ")

    if data == "0":
        return None

    root = Node(data)

    print(f"Enter left book of {data}:")
    root.left = create()

    print(f"Enter right book of {data}:")
    root.right = create()

    return root


def preorder(root):
    if root is not None:
        print(root.data, end=" | ")
        preorder(root.left)
        preorder(root.right)


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" | ")
        inorder(root.right)


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" | ")


root = create()

print("\nPostorder:")
postorder(root)

print("\nPreorder:")
preorder(root)

print("\nInorder:")
inorder(root)
