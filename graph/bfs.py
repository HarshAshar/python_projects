from collections import defaultdict

class Graph:

    # constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, s):
        # s is the source node
        
        # create a list visited nodes. Start with False
        visited = [False] * (max(self.graph) + 1)

        # create a queue
        queue = []

        # start with the root node, so append and mar as visited
        queue.append(s)
        visited[s] = True

        while queue:
            # dequeue a vertex
            s = queue.pop(0)
            print(s, end = " ")

            # Get all adjacent vertices of the dequeued vertex s.
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


# Create a graph
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is the Breadth First Traversal starting from vertex 2:")

g.bfs(2)