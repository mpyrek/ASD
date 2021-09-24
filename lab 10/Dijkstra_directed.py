from queue import PriorityQueue


#złożoność O(Elog(V))

def dijkstra(G,s):
	parent=[None for i in range(len(G))]
	distance = [ float('inf') for i in range(len(G))]
	Q=PriorityQueue()
	not_visted=len(G)
	#dist,idx,par
	Q.put((0,s,None))
	while Q.empty()==False and not_visted>0:
		dist , v, par = Q.get()
		if distance[v]>dist: #tylko raz to uaktualnimy
				parent[v]=par
				not_visted=not_visted-1
				distance[v]=dist
				for el in G[v]:
					Q.put((dist+el[1],el[0],v))
	
	return distance

G = [[(1,0), (2,1)],
[(3,1), (2,0)],
[(3,0)],
[]]

graph = [[[1, 1], [2, 5]],
         [[0, 1], [4, 7], [3, 8], [2, 2]],
         [[0, 5], [1, 2], [3, 3]],
         [[2, 3], [1, 8], [4, 87]],
         [[1, 7], [3, 87]]]


print( dijkstra( G, 0 ) ) # wypisze [None,0,1,2]

M=[[1e6,0,1,1e6],
[1e6,1e6,0,1],
[1e6,1e6,1e6,0],
[1e6,1e6,1e6,1e6]]

#czy tu mozna nie uzywac koljeki?
def dijkstra_2(M,s):
	parent=[None]*len(M)
	distance=[float('inf')]*len(M)
	Q=PriorityQueue()
	not_visted=len(M)

	Q.put((0,s,None))

	while Q.empty()==False and not_visted>0:
		dist, v,par=Q.get()
		if distance[v]>dist:
			distance[v]=dist
			parent[v]=par
			not_visted=not_visted-1
			for i in range(len(M[v])):
				if M[v][i] != 1e6:
					Q.put((dist+M[v][i],i,v))
			
	return distance

print(dijkstra_2(M,0))
