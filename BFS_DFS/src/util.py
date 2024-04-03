import networkx as nx
import matplotlib.pyplot as plt


def display_graph1(graph, traversal_path=None, title="Graph"):
    G = nx.Graph(graph)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='black', linewidths=1,
            font_size=15)

    if traversal_path:
        nx.draw_networkx_nodes(G, pos, nodelist=traversal_path, node_color='red', node_size=1500)

    plt.title(title)
    plt.show()


def display_graph(graph, traversal_path=None, title="Graph"):
    G = nx.Graph(graph)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='black', linewidths=1,
            font_size=15)

    if traversal_path:
        traversal_edges = [(traversal_path[i], traversal_path[i + 1]) for i in range(len(traversal_path) - 1)]
        traversal_graph = nx.Graph()
        traversal_graph.add_edges_from(traversal_edges)
        nx.draw_networkx_edges(traversal_graph, pos, edge_color='red', width=2)

    plt.title(title)
    plt.show()
