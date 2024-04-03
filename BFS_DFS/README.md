# Graph Traversal Algorithms (BFS and DFS)

This Python project demonstrates the implementation and visualization of Breadth-First Search (BFS) and Depth-First Search (DFS) algorithms for traversing graphs. The project includes separate files for graph representation, BFS algorithm, DFS algorithm, and utility functions for displaying graphs.

## Explanation

### Graph Representation

A graph $G$ is represented as a collection of vertices and edges. The vertices are denoted as $v_1, v_2, ..., v_n$, where $n$ is the number of vertices. An edge $(v_i, v_j)$ connects vertex $v_i$ to vertex $v_j$.

### Breadth-First Search (BFS)

BFS is an algorithm for traversing or searching tree or graph data structures. It starts at the root (selecting some arbitrary node as the root in the case of a graph) and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.

1. Begin with a start vertex $v_s$ and initialize a queue $Q$.
2. Enqueue the start vertex $v_s$ into $Q$ and mark it as visited.
3. While $Q$ is not empty, dequeue a vertex $v$ from $Q$:
   - Visit $v$.
   - Enqueue all adjacent vertices of $v$ into $Q$ if they are not already visited and mark them as visited.
4. Continue until $Q$ is empty.

- **Time Complexity**: $O(|V| + |E|)$, where $|V|$ is the number of vertices and $|E|$ is the number of edges.
- **Space Complexity**: $O(|V|)$, where $|V|$ is the number of vertices.

### Depth-First Search (DFS)

DFS is an algorithm for traversing or searching tree or graph data structures. It starts at the root (selecting some arbitrary node as the root in the case of a graph) and explores as far as possible along each branch before backtracking.

1. Begin with a start vertex $v_s$ and initialize a stack $S$.
2. Push the start vertex $v_s$ onto $S$ and mark it as visited.
3. While $S$ is not empty, pop a vertex $v$ from $S$:
   - Visit $v$.
   - Push all unvisited adjacent vertices of $v$ onto $S$ and mark them as visited.
4. Continue until $S$ is empty.

- **Time Complexity**: $O(|V| + |E|)$, where $|V|$ is the number of vertices and $|E|$ is the number of edges.
- **Space Complexity**: $O(|V|)$, where $|V|$ is the number of vertices.

## Graphs

### Initial Graph (Before)

![Initial Graph ($G$)](https://github.com/yehonatanke/Algorithms/blob/main/BFS_DFS/output/g.png)
![Initial Graph ($G_1$)](https://github.com/yehonatanke/Algorithms/blob/main/BFS_DFS/output/g1.png)


### BFS Final Graph (After)

![BFS Final Graph($G$)](https://github.com/yehonatanke/Algorithms/blob/main/BFS_DFS/output/gbfstree.png)
![BFS Final Graph($G_1$)](https://github.com/yehonatanke/Algorithms/blob/main/BFS_DFS/output/g1bfstree.png)

### DFS Final Graph (After)

![DFS Final Graph($G$)](https://github.com/yehonatanke/Algorithms/blob/main/BFS_DFS/output/gdfstree.png)
![DFS Final Graph($G_1$)](https://github.com/yehonatanke/Algorithms/blob/main/BFS_DFS/output/g1dfstree.png)
