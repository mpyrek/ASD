G1=[[0,1,0,0],[1,0,1,1],[0,1,0,1],[0,1,1,0]]

import glob

class Node:
    def __init__(self):
        self.next=None
        self.val=None

class Stack3:
    def __init__(self):
        self.top=Node()

    def push(self,x):
        N=Node()
        N.val=x
        N.next=self.top.next
        self.top.next=N

    def pop(self):
        N=self.top.next
        self.top.next=N.next
        return N.val

    def is_empty(self):
        return self.top.next==None


def print_node(S):
	if S.top.next==None: return
	v=S.top

	while v.next!=None:
		print(v.next.val)
		v=v.next

class V:
	def __init__(self,i):
		self.i=i
		self.parent=None
		self.visted=False
		self.entry=None
		self.process=None

def DFS(G):
	global f
	f=False

	def DFS_F(G,u,v):
		global f
		for k in G[v]:
			if T[k].visted==False:
				if u.i in G[k]:
					f=True
					return f
				T[k].visted=True
				DFS_F(G,u,k)		
		return f

	T=[None]*len(G)
	for i in range(len(G)): T[i]=V(i)
	
	for k in range(len(G)):
		for i in range(k,len(G)): T[i].visted=False
		T[k].visted=True
		#znajdujemy w sąsiednim wierzchołku wierzchołek który nie był jeszcze odwiedzony, mp. k=0 w sąsiadach k jest 1, a z 1  mozemy isc do 0-true i 2-false=> idziemy do 2
		p=0
		for t in G[k]:
			if p==0:
				if T[t].visted==False:
					p=t
					T[t].visted=True
		DFS_F(G,T[k],p)
		if f: return f		
	return f #False


G = [[1],[0,2],[1,3],[1,2]]
print(DFS(G))

