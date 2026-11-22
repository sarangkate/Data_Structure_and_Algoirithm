class HashTable:
    def __init__(self, size, replace):
        self.size = size
        self.table = [None] * size
        self.replace = replace

    def insert(self, key):
        home = key % self.size

        if key in self.table:
            print("Duplicate key:", key)
            return

        if self.replace and self.table[home] is not None:
            old = self.table[home]

            if old % self.size != home:
                self.table[home] = key
                for i in range(1, self.size):
                    pos = (home + i) % self.size
                    if self.table[pos] is None:
                        self.table[pos] = old
                        return
                self.table[home] = old
                print("Hash table is full.")
                return

        for i in range(self.size):
            pos = (home + i) % self.size
            if self.table[pos] is None:
                self.table[pos] = key
                return

        print("Hash table is full.")

    def search(self, key):
        home = key % self.size
        for i in range(self.size):
            pos = (home + i) % self.size
            if self.table[pos] is None:
                break
            if self.table[pos] == key:
                return pos
        return -1

    def display(self):
        print("\nIndex\tKey")
        for i in range(self.size):
            print(i, "\t", self.table[i] if self.table[i] is not None else "EMPTY")


size = int(input("Enter hash table size: "))
choice = int(input("1. Without replacement  2. With replacement: "))

if size <= 0 or choice not in (1, 2):
    print("Invalid input.")
else:
    h = HashTable(size, choice == 2)

    n = int(input("Enter number of keys: "))
    for i in range(n):
        key = int(input("Enter key: "))
        h.insert(key)

    h.display()

    key = int(input("\nEnter key to search: "))
    pos = h.search(key)

    if pos != -1:
        print("Key found at index", pos)
    else:
        print("Key not found")