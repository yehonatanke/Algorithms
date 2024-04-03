from collections import deque


def bfs(graph, start):
    if start not in graph:
        raise ValueError("Starting vertex not in graph")

    visited = set()
    queue = deque([start])
    traversal_path = []

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            traversal_path.append(vertex)
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return traversal_path
