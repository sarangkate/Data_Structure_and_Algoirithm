class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[0] * n for _ in range(n)]

    def add_edge(self, u, v, w):
        self.adj[u][v] = w
        self.adj[v][u] = w

    def prim(self, start):
        key = [float('inf')] * self.n
        parent = [-1] * self.n
        visited = [False] * self.n
        key[start] = 0

        for _ in range(self.n):
            u = -1
            for i in range(self.n):
                if not visited[i] and (u == -1 or key[i] < key[u]):
                    u = i

            if key[u] == float('inf'):
                print("Graph is disconnected.")
                return

            visited[u] = True

            for v in range(self.n):
                w = self.adj[u][v]
                if w > 0 and not visited[v] and w < key[v]:
                    key[v] = w
                    parent[v] = u

        cost = 0
        print("\nMST Edges:")
        for v in range(self.n):
            if parent[v] != -1:
                w = self.adj[v][parent[v]]
                print(parent[v], "-", v, ":", w)
                cost += w

        print("Total Minimum Cost:", cost)


n = int(input("Enter number of vertices: "))
g = Graph(n)

e = int(input("Enter number of edges: "))
for i in range(e):
    u, v, w = map(int, input("Enter edge (u v weight): ").split())
    g.add_edge(u, v, w)

start = int(input("Enter starting vertex: "))
g.prim(start)