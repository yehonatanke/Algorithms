# class Graph:
#     def __init__(self):
#         self.adj_list = {}
#
#     def add_vertex(self, vertex):
#         if vertex not in self.adj_list:
#             self.adj_list[vertex] = []
#
#     def add_edge(self, vertex1, vertex2):
#         if vertex1 in self.adj_list and vertex2 in self.adj_list:
#             self.adj_list[vertex1].append(vertex2)
#             self.adj_list[vertex2].append(vertex1)
#         else:
#             raise ValueError("One or both vertices not in graph")
#
#     def get_adj_list(self):
#         return self.adj_list
#
#     def vertex_exists(self, vertex):
#         return vertex in self.adj_list
#
#     def edge_exists(self, vertex1, vertex2):
#         return vertex2 in self.adj_list[vertex1]


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)
        else:
            raise ValueError("One or both vertices not in graph")

    def get_adj_list(self):
        return self.adj_list

    def vertex_exists(self, vertex):
        return vertex in self.adj_list

    def edge_exists(self, vertex1, vertex2):
        return vertex2 in self.adj_list[vertex1]

    # @classmethod
    # def create_graph(cls, num_vertices):
    #     graph = cls()
    #     for i in range(1, num_vertices + 1):
    #         graph.add_vertex(f'v_{i}')
    #     return graph

    @classmethod
    def create_graph(cls, num_vertices):
        graph = cls()
        for i in range(1, num_vertices + 1):
            vertex = f'v_{i}'
            graph.add_vertex(vertex)
            # Connect the vertex to all previously added vertices
            for j in range(1, i):
                other_vertex = f'v_{j}'
                graph.add_edge(vertex, other_vertex)
        return graph
