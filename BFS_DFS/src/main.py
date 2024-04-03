from graph import Graph
from bfs import bfs
from dfs import dfs
from util import display_graph


def main():
    # Create a personalize graph
    g1 = Graph()
    g1.add_vertex('A')
    g1.add_vertex('B')
    g1.add_vertex('C')
    g1.add_vertex('D')
    g1.add_vertex('E')
    g1.add_vertex('F')

    # creating a graph with 6 vertices
    num_vertices = 6
    g = Graph.create_graph(num_vertices)

    # Display the initial graph
    print("Initial Graph:")
    display_graph(g.get_adj_list(), title="Initial Graph (g)")
    display_graph(g1.get_adj_list(), title="Initial Personalize Graph (g1)")

    # Add edges to personalize graph
    g1.add_edge('A', 'B')
    g1.add_edge('A', 'C')
    g1.add_edge('B', 'D')
    g1.add_edge('B', 'E')
    g1.add_edge('C', 'F')
    g1.add_edge('E', 'A')

    # Display the graph after adding edges
    print("\nGraph after adding edges:")
    display_graph(g1.get_adj_list(), title="Graph after adding edges")

    # Perform BFS and DFS traversals on g
    bfs_traversal = bfs(g.get_adj_list(), 'v_1')
    dfs_traversal = dfs(g.get_adj_list(), 'v_1')

    # Perform BFS and DFS traversals on g1
    bfs_traversal_g1 = bfs(g1.get_adj_list(), 'E')
    dfs_traversal_g1 = dfs(g1.get_adj_list(), 'E')

    # Display BFS traversal on the graph
    print("\nBFS Traversal:", bfs_traversal)
    display_graph(g.get_adj_list(), traversal_path=bfs_traversal, title="BFS Traversal")

    # Display DFS traversal on the graph
    print("\nDFS Traversal:", dfs_traversal)
    display_graph(g.get_adj_list(), traversal_path=dfs_traversal, title="DFS Traversal")

    # Display BFS traversal on the graph
    print("\nBFS Traversal:", bfs_traversal_g1)
    display_graph(g1.get_adj_list(), traversal_path=bfs_traversal_g1, title="BFS Traversal")

    # Display DFS traversal on the graph
    print("\nDFS Traversal:", dfs_traversal_g1)
    display_graph(g1.get_adj_list(), traversal_path=dfs_traversal_g1, title="DFS Traversal")


if __name__ == "__main__":
    main()
