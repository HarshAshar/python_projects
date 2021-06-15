# The Floyd Warshall Algorithm is for solving the All Pairs Shortest Path problem.
# The problem is to find shortest distances between every pair of vertices in a given edge weighted directed Graph.

import sys

# Number of vertices
V = 4

INF = sys.maxsize

def floydWarshall(graph):
    # dist[][] will be the output matrix that will finally have the shortest distances between every pair of vertices
    # initializing the solution matrix same as input graph matrix OR we can say that the initial values of shortest 
    # distances are based on shortest paths considering no intermediate vertices

    dist = list(map(lambda i: list(map(lambda j: j,i)), graph))

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    
    printSolution(dist)

def printSolution(dist):
    print("Following matrix shows the shortest distances between each pair of vertices")
    
    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                print("INF", end = "\t")
            else:
                print(dist[i][j], end = "\t")
        
        print("")


graph = [
[0,   5,   INF, 10],
[INF, 0,   3,   INF],
[INF, INF, 0,   1],
[INF, INF, INF, 0]]

floydWarshall(graph)