#Dana jest struktura realizująca listę jednokierunkową:
class Node:
	def __init__( self, val ):
		self.next = None
		self.val = val
#Proszę napisać funkcję, która mając na wejściu ciąg tak zrealizowanych posortowanych list scala je w jedną posortowaną listę (składającą się z tych samych elementów). Przykład Dla tablicy [[0,1,2,4,5],[0,10,20],[5,15,25]] - po przekształceniu jej elementów z Python’owskich list na listy jednokierunkowe - wynikiem powinna być lista jednokierunkowa, która po przekształceniu jej na listę Python’owską przyjmie postać [0,0,1,2,4,5,5,10,15,20,25].

A=[[0,1,2,4,5],[0,10,20],[5,15,25]]

class Heap:
	def __init__(self, oper=lambda x, y: x < y):
		self.tab=[]
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
		if l<=size and self.oper(tab[l].head.val,tab[idx].head.val):
			idx=l
		if r<=size and self.oper(tab[r].head.val,tab[idx].head.val):
			idx=r
		if idx == i:
			return
		tab[idx], tab[i] = tab[i], tab[idx]
		self.heapify(idx)


	def bulid_heap(self, tab):
		size=len(tab)
		self.tab=[size] + tab
		for i in range(size // 2, 0, -1):
			self.heapify(i)
	
	def pop_top(self):
		size=self.len()
		self.tab[1]=self.tab[size]
		self.tab.pop()
		self.tab[0]=self.tab[0]-1

	def pop_el(self):
		x=self.get_top().head
		if self.get_top().head.next!=None:
			self.get_top().head=self.get_top().head.next
		else:
			self.pop_top()

		self.heapify(1)
		return x


	def heapify_up(self,i):
		p=self.p(i)
		if p<1:
			return
		tab=self.tab
		if self.oper(tab[i].head.val,tab[p].head.val):
			tab[i],tab[p] = tab[p],tab[i]
			self.heapify_up(p)


	def push(self,w):
		self.tab.append(w)
		self.tab[0] = self.tab[0]+1 
		self.heapify_up(self.len())

	def heapsort(self,tab):
		self.bulid_heap(A)
		for i in range(self.len(),0,-1):
			A[i-1]=self.pop_top() 
		return A



class List:
	def __init__(self):
		self.head=None
		self.tail=None

	def push(self,w):
		N=Node(w)
		if self.head==None:
			self.head=N
			self.tail=N
		else:
			self.tail.next=N
			self.tail=N

	def push_node(self,N):
		if self.head==None:
			self.head=N
			self.tail=N

		else:
			self.tail.next=N
			self.tail=N

	def is_empty(self):
		return self.head==None

	def has_one_el(self):
		return self.head==self.tail

	def print_list(self):
		h=self.head
		while h:
			print(h.val)
			h=h.next


def make_list(T):
	L=List()
	for i in range(len(T)):
		L.push(T[i])

	return L


def scal_k_posortowanych_T(T):
	for i in range(len(T)):
		T[i]=make_list(T[i])

	H=Heap()
	H.bulid_heap(T)

	K=[]

	while H.len()!=0:
		x=H.pop_el()
		K.append(x.val)

	print(K)


scal_k_posortowanych_T(A)