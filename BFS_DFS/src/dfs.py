def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    traversal_path = []

    if start not in visited:
        traversal_path.append(start)
        visited.add(start)
        for neighbor in graph[start]:
            traversal_path.extend(dfs(graph, neighbor, visited))

    return traversal_path
