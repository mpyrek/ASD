
class V:
	def __init__(self,i):
		self.i=i
		self.parent=None
		self.visted=False
		self.entry=None
		self.process=None

time=0
def DFS( G ):
# G to lista list z informacją o istnieniu krawędzi
# G[i] to lista numerów wierzchołków, które są połączone
# krawędzią z wierzchołkiem i
	def DFS_Visit(u):
		global time
		time=time+1
		u.entry=time
		u.visted=True

		for v in G[u.i]:
			if T[v].visted==False:
				T[v].parent=u.i
				DFS_Visit(T[v])
		time=time+1
		u.process=time
	
	T=[0]*len(G)
	for i in range(len(G)):
		T[i]=V(i)

	for v in range(len(G)):
		if T[v].visted==False:
			DFS_Visit(T[v])

	S=[0]*len(T)
	for i in range(len(G)):
		S[i]=T[i].parent
	return S
# elementarny test. Może wypisać np.
# [None,0,1,2]
G = [[1,2],[0,2,3],[3,1,0],[]]
print(DFS(G))

#dla reprezentacji macierzowej

class V:
	def __init__(self,i):
		self.i=i
		self.parent=None
		self.visted=False
		self.entry=None
		self.process=None

time=0
def DFS( G ):
# G to lista list z informacją o istnieniu krawędzi
# G[i] to lista numerów wierzchołków, które są połączone
# krawędzią z wierzchołkiem i
	def DFS_Visit(G,u):
		global time
		time=time+1
		u.entry=time
		u.visted=True

		for v in range(len(G[u.i])):
			if G[u.i][v]==1 and T[v].visted==False:
				T[v].visted=True
				T[v].parent=u.i
				DFS_Visit(G,T[v])
		time=time+1
		u.process=time
	
	T=[0]*len(G)
	for i in range(len(G)):
		T[i]=V(i)

	for v in range(len(G)):
		if T[v].visted==False:
			DFS_Visit(G,T[v])

	S=[0]*len(T)
	for i in range(len(G)):
		S[i]=(T[i].i,T[i].entry, T[i].process)
	return S
