class Graph:
    def __init__(self):
        self.v = 0
        self.e = 0
        self.G = [[0 for i in range(9)] for j in range(9)]

    def create(self):
        self.v = int(input("Enter no of vertices: "))
        self.e = int(input("Enter no of edges: "))

        for i in range(self.e):
            print("Enter Edge", i + 1)

            u = int(input("Enter start vertex: "))
            v = int(input("Enter end vertex: "))

            self.G[u][v] = 1
            self.G[v][u] = 1

    def display(self):
        print("Adjacency Matrix:")

        for i in range(self.v):
            for j in range(self.v):
                print(self.G[i][j], end=" ")
            print()

class Stack:
    def __init__(self):
        self.top = -1
        self.ST = [0] * 100

    def push(self, x):
        if self.top == 99:
            print("Stack is overflow..")
            return

        self.top = self.top + 1
        self.ST[self.top] = x

    def pop(self):
        if self.top == -1:
            print("Nothing to print..")
            return None

        x = self.ST[self.top]
        self.top = self.top - 1

        return x


def dfs(ob, start):
    visited = [False] * ob.v

    s = Stack()
    s.push(start)

    while s.top != -1:
        u = s.pop()

        if visited[u] == False:
            print(u, end=" ")
            visited[u] = True

            # Reverse order so smaller vertex is processed first
            for v in range(ob.v - 1, -1, -1):
                if ob.G[u][v] == 1 and visited[v] == False:
                    s.push(v)
# Main
ob = Graph()

ob.create()

ob.display()

start = int(input("Enter start vertex: "))

print("DFS:", end=" ")
dfs(ob, start)
