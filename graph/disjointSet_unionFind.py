from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def find_parent(self, parent, i):
        if parent[i] == -1:
            return i
        if parent[i] != -1:
            return self.find_parent(parent, parent[i])

    def union(self, parent, x, y):
        parent[x] = y

    def isCyclic(self):
        
        # Allocate memory for creating V subsets and
        # Initialize all subsets as single element sets
        parent = [-1] * (self.V)

        # Iterate through all edges of graph, find subset of both
        # vertices of every edge, if both subsets are same, then
        # there is cycle in graph.

        for i in self.graph:
            for j in self.graph[i]:
                print("Edge:", i, j)

                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)

                print(x, y)
                print(parent)

                if x == y:
                    return True
                self.union(parent, x, y)


g = Graph(3)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)

if g.isCyclic():
    print("Graph contains a cycle")
else:
    print("Graph does not contain a cycle")