class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
def insert(root, x):
    if root is None:
        return Node(x)
    if x > root.data:
        root.right = insert(root.right, x)
    else:
        root.left = insert(root.left, x)
    return root
def create():
    root = None
    while True:
        x = int(input("Enter data to create node (0 to stop): "))
        if x == 0:
            break
        else:
            root = insert(root, x)
    return root
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

class Queue:
    def __init__(self):
        self.F = -1
        self.R = -1
        self.Q = [0] * 5
    def insert(self, x):
        if self.R == 4:
            print("Queue is overflow.")
            return
        self.R = self.R + 1
        self.Q[self.R] = x

        if self.F == -1:
            self.F = 0
    def delete(self):
        if self.F == -1:
            print("Nothing to print.")
            return None
        y = self.Q[self.F]
        if self.F == self.R:
            self.F = -1
            self.R = -1
        else:
            self.F = self.F + 1
        return y

def level_wise(root):
    if root is None:
        return
    q = Queue()
    q.insert(root)
    while q.F != -1:
        r = q.delete()
        print(r.data, end=" ")
        if r.left is not None:
            q.insert(r.left)
        if r.right is not None:
            q.insert(r.right)

def height(root):
    if root is None:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    return 1 + max(left_height, right_height)

def leaf_nodes(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        print(root.data, end=" ")
        return
    leaf_nodes(root.left)
    leaf_nodes(root.right)

def copy_tree(root):
    if root is None:
        return None
    new_root = Node(root.data)
    new_root.left = copy_tree(root.left)
    new_root.right = copy_tree(root.right)
    return new_root

root = create()
print("\nOriginal BST - Inorder:")
inorder(root)
print("\n\nOriginal BST - Level Order:")
level_wise(root)
print("\n\nHeight of Original BST:", height(root))
print("\nLeaf Nodes of Original BST:")
leaf_nodes(root)

new_root = copy_tree(root)
print("\n\nCopied BST - Level Order:")
level_wise(new_root)
print("\n")
