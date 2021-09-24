# Ścieżka Hamiltona to ścieżka przechodząca przez wszystkie wierzchołki w grafie, przez każdy dokładnie raz. W ogólnym grafie znalezienie ścieżki Hamiltona jest problemem NP-trudnym. Proszę podać algorytm, który stwierdzi czy istnieje ścieżka Hamiltona w acyklicznym grafie skierowanym


#sortujemy topologicznie a nastepnie sprawdzamy czy istnieje sciezka w danej klejności

class V:
	def __init__(self,i):
		self.i=i
		self.parent=None
		self.visted=False
		self.entry=None
		self.process=None

time=0
def Hamilton_path( G ):
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
		S.append(u.i)
		time=time+1
		u.process=time
	
	T=[0]*len(G)
	for i in range(len(G)):
		T[i]=V(i)
	S=[]
	for v in range(len(G)):
		if T[v].visted==False:
			DFS_Visit(G,T[v])
	S.reverse()

	for i in range(len(S)-1):
		if G[S[i]][S[i+1]]==1: continue	
		else: return False
	print(S)
	return True


G=[[0,1,0,0,1],[0,0,1,1,0],[0,0,0,1,1],[0,0,0,0,1],[0,0,0,0,0]]

print(Hamilton_path(G))
	