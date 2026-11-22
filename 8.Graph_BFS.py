from collections import deque

V, E = map(int, input().split())
graph = [[] for _ in range(V)]

for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for neighbours in graph:
    neighbours.sort()

start = int(input())

print("Adjacency List:")
for vertex in range(V):
    print(vertex, ":", *graph[vertex])

def bfs(graph, start):
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True
    order = []

    while queue:
        u = queue.popleft()
        order.append(u)
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)

    return order

print("BFS Traversal:")
print(*bfs(graph, start))
