from queue import PriorityQueue

## lista sąsiedztwa

graph = [[[1, 1], [2, 5]],
         [[0, 1], [4, 7], [3, 8], [2, 2]],
         [[0, 5], [1, 2], [3, 3]],
         [[2, 3], [1, 8], [4, 87]],
         [[1, 7], [3, 87]]]

def dijkstra(graph, s):
    q = PriorityQueue()
    dist = [float('inf') for _ in range(len(graph))]
    counter = len(graph)
    q.put((0, s))

    while not q.empty() and counter > 0:
        d, v = q.get()
        if d < dist[v]: # to się wykona tylko raz dla każdego wierzchołka
            counter -= 1
            dist[v] = d
            for edge in graph[v]:
                neighbor, edge_len = edge
                q.put((d + edge_len, neighbor))
    return dist
        

#print(dijkstra(graph, 0))


G=[[-1,10,2,2,],
    [10,-1,5,-1],
    [2,5,-1,8],
    [2,-1,8,-1]]
    
def matrix_dijkstra(G,a,b):
    Dist=[float('inf')]*len(G)
    Vis=[False]*len(G)

    Dist[a]=0

    for i in range(len(G)):
        minn=float('inf')
        idx_of_min=None
        for j in range(len(G)):
            if minn>Dist[j] and Vis[j]==False:
                minn=Dist[j]
                idx_of_min=j
        
        Vis[idx_of_min]=True

        for j in range(len(G)):
            if G[idx_of_min][j] !=-1 and Vis[j]==False:
                Dist[j]=G[idx_of_min][j]+Dist[idx_of_min]

    return Dist

print(matrix_dijkstra(G,1,3))