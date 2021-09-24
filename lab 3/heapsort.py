
#kopiec typu min
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


	def bulid_heap(self, tab):
		size=len(tab)
		self.tab=[size] + tab
		for i in range(size // 2, 0, -1):
			self.heapify(i)
	
	def pop_top(self):
		size=self.len()
		top=self.get_top()
		self.tab[1]=self.tab[size]
		self.tab.pop()
		self.tab[0]=self.tab[0]-1
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
		self.tab[0] = self.tab[0]+1 
		self.heapify_up(self.len())

	def heapsort(self,tab):
		self.bulid_heap(tab)
		for i in range(self.len(),0,-1):
			tab[i-1]=self.pop_top() 
		return tab


A=[5,1,-2,3,5,9,-4]
heap=Heap(lambda x,y: x>y)
A=heap.heapsort(A)
print(A)