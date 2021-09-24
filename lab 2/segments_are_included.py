#program znajdujący odc., w którym zawiera się jak najwięcej odcinków 

A=[[0,7],[2,6],[3,9],[5,7],[5,6]]
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




#O(n^2)
def find_max(A):
	n=len(A)
	max_count=0
	for i in range(0,n):
		tmp=A[i]
		count=0
		for j in range(i+1,n):
			if tmp[0]<=A[j][0] and tmp[1]>=A[j][1]:
				count=count+1
		max_count=max(count,max_count)

	return max_count

#print(find_max(A))


def find_max2(A):
	H=Heap(lambda x,y: x[0]>y[0])
	H.heapsort(A)

	last=A[0][0]
	count=1
	f=[]
	f.append((A[0][0],1))
	
	for i in range(1,len(A)):
		count+=1
		if A[i][0]==last:
			x=f.pop()
			f.append((A[i][0],count))
		else:
			last=A[i][0]
			f.append((A[i][0],count))


	j=0
	for i in range(len(A)):
		if f[j][0]!=A[i][0]:
			j=j+1
		A[i]=(A[i],f[j][1])
	

	H=Heap(lambda x,y: x[0][1]>y[0][1])
	H.heapsort(A)


	g=[]
	count=1
	last=A[0][0][1]
	g.append((A[0][0][1],A[0][1]-count))

	for i in range(1,len(A)):
		count+=1
		if A[i][0][1]==last:
			x=g.pop()
			g.append((A[i][0][1],count))
		else:
			last=A[i][0][1]
			g.append((A[i][0][1],count))
	
	j=0
	for i in range(len(A)):
		if g[j][0]!=A[i][0][1]:
			j=j+1
		A[i]=((A[i],g[j][1]))


	max_el=-1
	count=0
	max_count=0
	for i in range(len(A)):
		count=A[i][1]-A[i][0][1]
		if count>max_count:
			max_count=count
			max_el=A[i][0][0]

	return (max_el)


print(find_max2(A))