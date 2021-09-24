
# G to macierz opisująca graf: G[i][j]==1 jeśli jest wierzchołek z i do j. W przeciwnym razie G[i][j]=0, s to numer wierzchołka źródłowego,tu proszę umieścić swoją implementację elementarny test, powinien wypisać
# [(None,0), (0,1), (0,1), (2,2)]
# lub
# [(None,0), (0,1), (0,1), (1,2)]


G = [[0,1,1,0],[0,0,0,1],[0,1,0,1], [0,0,0,0]]
#print(BFS(G,0))

class Queue:
	def __init__(self,n,idx):
		self.S=[[None]*2 for i in range(n)]
		self.elements=0
		self.head=idx
		self.n=n

	def enqueue(self,x,d):
		if self.head+self.elements>=self.n:
			self.S[self.elements-(self.n-self.head)][0]=x
			self.S[self.elements-(self.n-self.head)][1]=d
			self.elements=self.elements+1
		else:
			self.S[self.head+self.elements][0]=x
			self.S[self.head+self.elements][1]=d
			self.elements=self.elements+1

	def dequeue(self):
		if self.head+self.elements>=self.n:
			self. elements=self.elements-1
			z=self.S[self.elements-(self.n-self.head)]
			if self.head+1==self.n:
				self.head=0
			else: self.head=self.head+1
			return z

		else:
			self.elements=self.elements-1
			z=self.S[self.head+self.elements]
			if self.head+1==self.n: 
				self.head=0
			else: self.head=self.head+1
			return z

	
	def is_empty(self):
		return self.elements==0


def BFS2(G,s):
	Q=Queue(len(G),0)
	T=[0]*len(G)

	for v in range(len(T)):
		T[v]=False
	
	Q.enqueue(None,0)

	while Q.is_empty()==False:
		for i in range(len(T)):
			if G[Q.head][i]==1:
				if T[i]==False:
					T[i]=True
					Q.enqueue(Q.head,Q.S[Q.head][1]+1)
		Q.dequeue()
	return(Q.S)

print(BFS2(G,0))


# druga impl
class Node:
	def __init__(self,x):
		self.next=None
		self.val=x

class Queue:
	def __init__(self):
		self.Q=Node(None)
		self.tail=Node(None)

	def enqueue(self,x):
		N=Node(x)
		
		if self.Q.next==None:
			N.next=self.Q.next
			self.Q.next=N
			self.tail.next=N
		else:
			self.tail.next.next=N
			self.tail.next=N
		
	def dequeue(self):
		z=self.Q.next.val
		self.Q.next=self.Q.next.next
		return z

	def is_empty(self):
		return self.Q.next==None

def BFS(G,s,T):
	Q=Queue()
	
	Q.enqueue(s)
	P=[s]
	T[s]=True
	
	while Q.is_empty()==False:
		u=Q.dequeue()
		
		for i in range(len(G)):
			
			if G[u][i]==1 and T[i]==False:
				T[i]=True
				Q.enqueue(i)
				P.append(i)
	return (P,T)



#implementacja dla list sąsiedztwa

from queue import Queue

def BFS_the_best(G):
	visted=[False]*len(G)
	parent=[None]*len(G)

	Q=Queue()
	Q.put(0)

	while Q.empty()==False:
		x=Q.get()
		for el in G[x]:
			if visted[el]==False:
				visted[el]=True
				parent[el]=x
				Q.put(el)
				
	for i in range(len(G)):
		print(i,visted[i],parent[i])

BFS_the_best(G)