from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
        
    def addEdge(self, u, v):
        self.graph[u].append(v)

class Subset:
    
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank

def find(subsets, node):
    if subsets[node].parent != node:
        subsets[node].parent = find(subsets, subsets[node].parent)
    return subsets[node].parent

def union(subsets, u, v):
    # Attach smaller rank tree under root
    # of high rank tree(Union by Rank)

    if subsets[u].rank > subsets[v].rank:
        subsets[v].parent = u
    elif subsets[v].rank > subsets[u].rank:
        subsets[u].parent = v
    # If ranks are same, then make one as
    # root and increment its rank by one
    else:
        subsets[v].parent = u
        subsets[u].rank += 1

def isCyclic(g):
    
    subsets = []
    for u in range(g.V):
        subsets.append(Subset(u, 0))

    # Iterate through all edges of graph,
    # find sets of both vertices of every
    # edge, if sets are same, then there
    # is cycle in graph.

    for u in g.graph:
        u_rep = find(subsets, u)

        for v in g.graph[u]:
            v_rep = find(subsets, v)

            print("u_rep, v_rep: (", u_rep, v_rep, ")")

            if u_rep == v_rep:
                return True
            else:
                union(subsets, u_rep, v_rep)
            





g = Graph(3)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(0, 2)

if isCyclic(g):
    print("Graph contains a cycle")
else:
    print("Graph does not contain a cycle")