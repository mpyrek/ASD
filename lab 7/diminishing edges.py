#Zadanie 6. (malejące krawędzie) (implementacja) Dany jest graf G = (V, E), gdzie każda krawędź ma wagę ze zbioru {1, . . . , |E|} (wagi krawędzi są parami różne). Proszę zaproponować algorytm, który dla danych wierzchołków x i y sprawdza, czy istnieje ścieżka z x do y, w której przechodzimy po krawędziach o coraz mniejszych wagach


G=[[0,3,4,0],[3,0,0,4],[4,0,0,2],[0,4,2,0]]

T=[False]*len(G)



class Heap:
	def __init__(self, oper=lambda x, y: x < y):
		self.tab = [0]
		self.oper=oper
	
	def l(self,i):
		return 2*i

	def r(self,i):
		return 2*i+1

	def p(self,i):
		return i//2

	def len(self):
		return self.tab[0]

	def get_top(self):
		if self.len()==0:
			return None
		return self.tab[1]

	def heapify(self,i):
		size=self.len()
		tab=self.tab
		l=self.l(i)
		r=self.r(i)

		idx=i
		if l<=size and self.oper(tab[l],tab[idx]):
			idx=l
		if r<=size and self.oper(tab[r],tab[idx]):
			idx=r
		if idx == i:
			return
		tab[idx], tab[i] = tab[i], tab[idx]
		self.heapify(idx)


	def make_heap(self, tab):
		size=len(tab)
		self.tab=[size] + tab
		for i in range(size // 2, 0, -1):
			self.heapify(i)
	
	def pop_top(self):
		size=self.len()
		top=self.get_top()
		self.tab[1]=self.tab[size]
		self.tab.pop()
		self.tab[0]-=1
		self.heapify(1)
		return top

	def heapify_up(self,i):
		p=self.p(i)
		if p<1:
			return
		tab=self.tab
		if self.oper(tab[i],tab[p]):
			tab[i],tab[p] = tab[p],tab[i]
			self.heapify_up(p)


	def push(self,w):
		self.tab.append(w)
		self.tab[0] += 1
		self.heapify_up(self.len())

#max heap

def BFS2(Z,s,y,T):
	heap1=Heap(lambda x,y: x > y)
	
	heap1.push((s,None))
	P=[s]


	while heap1.len()!=0:
		u=heap1.pop_top()
		T[u[0]]=True
		print(u)
		for i in range(len(Z)):
			if Z[u[0]][i]>0 and (u[1]==None or Z[u[0]][i]<=u[1]) and T[i]==False:
				heap1.push((i,Z[u[0]][i]))
				if i==y: return True
				P.append((i,u[0]))
			#print(heap1.tab)
	return False

G1=[[0,1,12,0,0],[1,0,0,9,8],[12,0,0,10,0],[0,9,10,0,0],[0,8,0,0,0]]

T1=[False]*len(G1)
print(BFS2(G1,0,4,T1))
print(BFS2(G,0,3,T))