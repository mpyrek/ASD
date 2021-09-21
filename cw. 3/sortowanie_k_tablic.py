#algorytm sortujący k tablic o łącznej długości n w jedną posortowaną tbalicze w  czasnie O(nlogk)

class Heap:
	def __init__(self,oper=lambda x,y: x<y):
		self.tab=[0]
		self.oper=oper
	def l(self, i):
		return i*2
	def r(self,i):
		return 2*i+1
	def p(self,i):
		return i//2
	def len(self):
		return self.tab[0]
	def get_top(self):
		if self.len()==0:
			return None
		x=self.tab[1]
		return x[1][x[0]]

	def heapify(self,i):
		size=self.len()
		tab=self.tab
		r=self.r(i)
		l=self.l(i)

		idx=i
		if l<=size and self.oper(tab[l],tab[idx]):
			idx=l
		if r<=size and self.oper(tab[r],tab[idx]):
			idx=r
		if idx==i:
			return 
		tab[idx],tab[i]=tab[i],tab[idx]
		self.heapify(idx)

	def make_heap(self,tab):
		size=len(tab)
		self.tab=[size]+tab
		for i in range(size//2,0,-1):
			self.heapify(i)

	def pop_top(self):
		tab=self.tab
		top=self.get_top()
		tab[1][0]+=1
		if tab[1][0]==len(tab[1][1]):
			del(tab[1])
			tab[0]-=1
		self.heapify(1)
		return top
	

	def heapify_up(self,i):
		p=self.p(i)
		if p<1:
			return
		tab=self.tab
		if self.oper(tab[i],tab[p]):
			tab[i],tab[p]=tab[p],tab[i]
			self.heapify_up(p)
	
	def push(self,w):
		self.tab.append(w)
		self.tab[0]+=1
		self.heapify_up(self.len())

C=[1,2,3,4,5,6]
B=[1,3,4,7]
A=[5,5,6,7,9]

k=3

def sort_k_tab(A,B,C):
	n=0
	T=[A,B,C]
	for tab in T:
		n+=len(tab)		#dłg wablicy wyjściowej

	t = [[0, tab] for tab in T]
	heap = Heap(oper=lambda x, y: x[1][x[0]] < y[1][y[0]])
	heap.make_heap(t)
	
	D=[0]*n		
	for i in range(n):
		D[i]=heap.pop_top()

	return(D)

print(sort_k_tab(A,B,C))