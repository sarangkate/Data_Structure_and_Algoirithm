class Node:
    def __init__(self, admission_no, name):
        self.admission_no = admission_no
        self.name = name
        self.left = None
        self.right = None


def insert(root, admission_no, name):
    if root is None:
        return Node(admission_no, name)

    if admission_no < root.admission_no:
        root.left = insert(root.left, admission_no, name)
    else:
        root.right = insert(root.right, admission_no, name)

    return root


def search(root, admission_no):
    if root is None:
        return None

    if root.admission_no == admission_no:
        return root

    if admission_no < root.admission_no:
        return search(root.left, admission_no)
    else:
        return search(root.right, admission_no)


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.admission_no, "-", root.name)
        inorder(root.right)


root = None

n = int(input("Enter number of students: "))

for i in range(n):
    admission_no = int(input("Enter admission number: "))
    name = input("Enter student name: ")

    root = insert(root, admission_no, name)


print("\nStudent Admission Records:")
inorder(root)

key = int(input("\nEnter admission number to search: "))

student = search(root, key)

if student is not None:
    print("Student Found:")
    print("Admission Number:", student.admission_no)
    print("Name:", student.name)
else:
    print("Student not found.")
