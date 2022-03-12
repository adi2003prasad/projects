from tkinter import N


class graph():
    def __init__(self, n, edges) -> None:
        self.graph = [[] for _ in range(n)]
        for x in range(n):
            self.graph[x[0]].append(x[1])


def bfs(graph, queue, discovered):
    if not queue:
        return
    v = queue.pop(0)
    print(v)
    if not discovered[v]:
        discovered[v] = True
        for x in graph.graph[v]:
            queue.append(x)
            bfs(graph, queue, discovered)


n = 15
queue = []
discovered = [false]*n
edges = [
    (10, 2), (10, 30), (10, 4), (2, 50), (2, 6), (5, 9),
    (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)
    # vertex 0, 13, and 14 are single nodes
]
g = graph(n, edges)
for x in range(n):
    if x not in:
    queue.append(x)
