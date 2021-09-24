A=[[3, 5, 6], [5, 6], [4], [4, 0], [3, 2, 6], [1, 0], [1, 0, 4]]
Z=[[0, 0, 0, 1, 0, 1, 1], [0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0, 0], [0, 0, 1, 1, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0], [1, 1, 0, 0, 1, 0, 0]]
G = [[0, 0, 0, 0, 1],[0, 0, 1, 0, 1],[1, 0, 0, 0, 0],[0, 0, 1, 0, 1],[0, 1, 0, 1, 0]]

A1=[[1, 3, 5], [0, 5], [4], [4, 0], [3, 2], [1, 0]]


# złożoność BFS- O(V+E) + przejscie po wszytkich wierzchołakch i krawędziach O(V+E) => 2O(V+E)-upraszczemy do O(V+E)
class Node:
    def __init__(self):
        self.next=None
        self.val=None

class Queue1:
	def __init__(self):
		self.Q=Node()
		self.tail=Node()

	def enqueue(self,x):
		N=Node()
		N.val=x
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


class V:
    def __init__(self,i):
        self.i=i
        self.visted=False
        self.parent=None
        self.entry=None

def BFS(G):
    Q=Queue1()
    T=[0]*len(G)
    for i in range(len(G)):
        T[i]=V(i)

    time=0
    Q.enqueue(0)
    T[0].visted=True
    T[0].entry=time


    while Q.is_empty()==False:
        x=Q.dequeue()
        time=T[x].entry+1
        for i in G[x]:
            if T[i].visted==False:
                T[i].visted=True
                Q.enqueue(i)
                T[i].parent=x
                T[i].entry=time

    for i in range(len(G)):
        for j in G[i]:
            if not (T[i].entry+1==T[j].entry or T[i].entry-1==T[j].entry):
                return False
    return True

#print(BFS(A1))
#print(BFS(A))

from queue import Queue

# to samo ale kolorujemhy krawędzie 
class V2:
    def __init__(self, i):
        self.i=i
        self.visted=False
        self.color=1

def BFS_2(G):
    T=[0]*len(G)
    Q=Queue()

    for i in range(len(G)):
        T[i]=V(i)

    T[0].visted=True
    T[0].color=1
    Q.put(0)

    while Q.empty==False:
        x=Q.get()
        for el in G[x]:
            if T[el].visted==False:
                T[el].visted=True
                T[el].color=(T[x].color+1)%2
                Q.put(el)
            else:
                if T[el].color == T[x].color:
                    return False

    return True

print(BFS(A1))
print(BFS(A))




# macierz sąsiedztwa 
#tym razem będizemy malować wierzchołki -1 kolor czerowny , 0 kolor czarny


class V1:
    def __init__(self,i):
        self.i=i
        self.visted=False
        self.color=None

def BFS_matrix(G):
    Q=Queue()
    Q.put(0)
    T=[0]*len(G)

    for i in range(len(G)):
        T[i]=V1(i)

    T[0].visted=True
    T[0].color=1

    while Q.empty()==False:
        x=Q.get()
        for i in range(len(G)):
            if G[x][i]==1:
                if T[i].visted==False:
                    T[i].visted=True
                    T[i].color=(T[x].color +1)%2
                else:
                    if T[i].color == T[x].color:
                        return True

    return True
#print(BFS_matrix(Z))
#print(BFS_matrix(G))