#Proszę zaimplementować funkcję count shortest paths(G,s,t), która oblicza ile różnych najkrótszych ścieżek prowadzi w grafie skierowanym G z wierzchołka s do wierzchołka t. Dwie ścieżki są różne jeśli różnią się choć jedną krawędzią. Graf G jest reprezentowany macierzowo (G[i][j] == True jeśli istnieje krawędź z i do j; G[i][j] = False w przeciwnym wypadku). Państwa kod powinien mieć następującą postać (będzie uruchamiany; proszę nie usuwać fragmentu testującego; sprawdzający może także dołożyć swoje testy):

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




def count_shortest_paths(G,s,t):
	Q=Queue()
	
	Q.enqueue(s)
	T=[[0,0,1] for i in range(len(G))]
	
	T[s][0]=1 #visted
	T[s][1]=0 #entry
	T[s][2]=1 #liczba ścieżek


	while Q.is_empty()==False:
		u=Q.dequeue()
		for i in range(len(G)):
			if G[u][i]:
				if T[i][0]==0:
					T[i][0]=1
					T[i][1]=T[u][1]+1
					T[i][2]=T[u][2]
					Q.enqueue(i)
				else:
					if T[u][1]+1==T[i][1]:
					   T[i][2]=T[i][2]*2

		print(T)
	return T[t][2]




G = [[False, True, True, False],
[False, False, True, True ],
[False, False, False, True ],
[False, False, False, False]]
print(count_shortest_paths( G, 0, 3 )) # wypisze 2

S=[[False,True,True,False,False,False,False],
   [False,False,False,True,False,False,False],
   [False,False,False,True,False,False,False],
   [False,False,False,False,True,True,False],
   [False,False,False,False,False,False,True],
   [False,False,False,False,False,False,True],
   [False,False,False,False,False,False,False]]

print(count_shortest_paths(S,0,6))
