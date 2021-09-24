G=[[1,2],[2,3],[3],[]]



class V:
	def __init__(self,i):
		self.i=i
		self.parent=None
		self.visted=False
		self.entry=None
		self.process=None



def Topological_sort(G):
	time=0
	def DFS_Visit(G,u):
		nonlocal time
		time=time+1
		u.entry=time
		u.visted=True

		for v in G[u.i]:
			if T[v].visted==False:
				T[v].parent=u.i
				DFS_Visit(G,T[v])
		time=time+1
		u.process=time
		L.append((u.i,u.entry,u.process))
	
	L=[]
	T=[0]*len(G)
	for i in range(len(G)):
		T[i]=V(i)

	for v in range(len(G)):
		if T[v].visted==False:
			DFS_Visit(G,T[v])

	L.reverse()
	print(L)
	

Topological_sort(G)