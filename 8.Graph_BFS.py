from collections import deque

class Graph:
    def __init__(self, v):
        self.adj = [[] for _ in range(v)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def bfs(self, start):
        visited = [False] * len(self.adj)
        q = deque([start])
        visited[start] = True

        while q:
            node = q.popleft()
            print(node, end=" ")

            for n in sorted(self.adj[node]):
                if not visited[n]:
                    visited[n] = True
                    q.append(n)


v = int(input("Enter number of vertices: "))
g = Graph(v)

e = int(input("Enter number of edges: "))
for i in range(e):
    u, v = map(int, input("Enter edge (u v): ").split())
    g.add_edge(u, v)

start = int(input("Enter starting vertex: "))
print("BFS Traversal:")
g.bfs(start)

