#8.Dana jest klasa :

#reprezentująca węzeł jednokierunkowego łańcucha odsyłaczowego, w którym wartości val poszczególnych węzłów zostały wygenerowane zgodnie z rozkładem jednostajnym na przedziale [a, b]. Napisz procedurę sort(first), która sortuje taką listę. Funkcja powinna być jak najszybsza.

class Node:
	def __init__(self):
		self.val = 0
		self.next = None


class List:
	def __init__(self):
		self.head=Node()
		self.tail=Node()

	def push(self,w):
		N=Node()
		N.val=w
		if self.head.next==None:
			self.head.next=N
			self.tail.next=N
		else:
			self.tail.next.next=N
			self.tail.next=N

	def push_node(self,N):
		if self.head.next==None:
			self.head.next=N
			self.tail.next=N
		else:
			self.tail.next.next=N
			self.tail.next=N

	def pop_front(self):
		self.head.next=self.head.next.next

	def pop_back(self):
		h=self.head
		while h.next.next:
			h=h.next
		h.next=None
		self.tail=h

	def is_empty(self):
		return self.head.next==None

	def reverse(self):
		self.tail.next=self.head.next
		prev=None
		tmp=self.head.next
		while tmp:
			next=tmp.next
			tmp.next=prev
			prev=tmp
			tmp=next
		self.head.next=prev

	def print_list(self):
		h=self.head
		while h.next:
			print(h.next.val)
			h=h.next

[3,6]

A9=Node()
A9.val=3.3
A=Node()
A.val=6
A1=Node()
A1.val=5.3
A2=Node()
A2.val=4.6
A3=Node()
A3.val=4.2
A4=Node()
A4.val=3.1

A9.next=A
A.next=A1
A1.next=A2
A2.next=A3
A3.next=A4

def quicker_sort_for_bucket(N):
	if N.is_empty() or N.head.next.next==None:
		return N

	pivot=N.head.next.val

	lT=List()
	eqT=List()
	gT=List()

	while N.head.next:
		k=N.head.next.next
		N.head.next.next=None
		if N.head.next.val<pivot:
			lT.push_node(N.head.next)
		elif N.head.next.val>pivot:
			gT.push_node(N.head.next)
		else:
			eqT.push_node(N.head.next)

		N.head.next=k
	
	return glue(glue(quicker_sort_for_bucket(lT),eqT),quicker_sort_for_bucket(gT))

def glue(L1,L2):
	if L1.is_empty():
		return L2
	if L2.is_empty():
		return L1

	L1.tail.next.next=L2.head.next
	L1.tail.next=L2.tail.next
	return L1




def sort(head,a,b):
	k=head
	count=0
	while k!=None:
		k=k.next
		count+=1

	norm=(b-a+1)
	
	F=[List() for i in range(count)]

	while head:
		x=(head.val-a)/norm
		F[int(x*count)].push_node(head)
		k=head.next
		head.next=None
		head=k


	for i in range(len(F)):
		if not F[i].is_empty(): 
			F[i]=quicker_sort_for_bucket(F[i])
	

	i=0
	while F[i].is_empty():
		i=i+1

	idx=i
	for i in range(idx+1,len(F)):
		if not F[i].is_empty():
			F[idx]=glue(F[idx],F[i])

	head=F[idx]

	head.print_list()


sort(A9,3,6)