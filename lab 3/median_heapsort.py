
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
		self.bulid_heap(A)
		for i in range(self.len(),0,-1):
			A[i-1]=self.pop_top() 
		return A




A=[5,1,-2,3,5,9,-4]


def add_el(h1,h2,x):
	l_t=h1.get_top()		#kopiec typu max
	r_t=h2.get_top()		#kopiec typu min

	if h1.len()==0:
		h1.push(x)
		return

	#pierwesza sytuacje gdy dłg obu heapów są sobie równe- pilnujemy dłg h1 i h2 : h1.len=h2.len || h1.len-1=h2.len
	if h1.len()==h2.len():
		if l_t>=x:
			h1.push(x)
		else:
			h1.push(h2.pop_top())
			h2.push(x)
	else:
		if l_t<=x:
			h2.push(x)
		else:
			h2.push(h1.pop_top())
			h1.push(x)


#funkcje znajdują środkowy el, w przypadku parzystej dłg. znajduj n-1/2

def find_median(A):
	if len(A)==0:
		return None

	heap_max=Heap(lambda x,y: x>y)
	heap_min=Heap()
	
	for i in range(len(A)):
		add_el(heap_max,heap_min,A[i])

	return heap_max.get_top()

#print(find_median(A))

def pop_median(A):
	if len(A)==0: 
		return None

	heap_max=Heap(lambda x,y: x>y)
	heap_min=Heap()
	
	for i in range(len(A)):
		add_el(heap_max,heap_min,A[i])

	if heap_max.len()==heap_min.len():
		mid=heap_max.pop_top()
		heap_max.push(heap_min.pop_top())
	else:
		mid=heap_max.pop_top()
	
	#zmieniamy nasze A żeby móc do końca usuwać el.
	A[0:heap_max.len()]=heap_max.tab[1:]
	A[heap_max.len():]=heap_min.tab[1:]
	h=Heap(lambda x,y: x>y)
	A=h.heapsort(A)
	print(A)
	return mid

#print(pop_median(A))
#print(pop_median(A))