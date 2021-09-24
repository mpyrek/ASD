#Zadanie 5. (dobry początek) Wierzchołek v w grafie skierowanym nazywamy dobrym początkiem jeśli każdy inny wierzchołek można osiągnąć scieżką skierowaną wychodzącą z v. Proszę podać algorytm, który stwierdza czy dany graf zawiera dobry początek.

G=[[],[],[0,1,3],[4,5],[],[4]]


class V:
	def __init__(self,i):
		self.i=i
		self.visted=False



def Good_start(G):

	def DFS_Visit(G,u):
		u.visted=True

		for v in G[u.i]:
			if T[v].visted==False:
				T[v].visted=True
				DFS_Visit(G,T[v])
		L.append(u.i)
	
	L=[]
	T=[0]*len(G)
	for i in range(len(G)):
		T[i]=V(i)

	for v in range(len(G)):
		if T[v].visted==False:
			DFS_Visit(G,T[v])


	for i in range(len(T)):
		T[i].visted=False
	
	x=L.pop()
	
	DFS_Visit(G,T[x])

	for i in range(len(T)):
		if T[i].visted==False : return False
	return x

print(Good_start(G))