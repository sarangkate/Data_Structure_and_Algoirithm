def heapify(a, n, i, choice):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if choice == 2:
        if l < n and a[l] > a[largest]:
            largest = l
        if r < n and a[r] > a[largest]:
            largest = r
    else:
        if l < n and a[l] < a[largest]:
            largest = l
        if r < n and a[r] < a[largest]:
            largest = r

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest, choice)


def heap_sort(a, choice):
    n = len(a)

    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i, choice)

    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, i, 0, choice)

    return a


n = int(input("Enter number of elements: "))
a = []

for i in range(n):
    a.append(int(input("Enter element: ")))

print("\n1. Min Heap - Descending")
print("2. Max Heap - Ascending")
choice = int(input("Enter your choice: "))

print("Original list:", a)

if choice in (1, 2):
    print("Sorted list:", heap_sort(a.copy(), choice))
else:
    print("Invalid choice")
