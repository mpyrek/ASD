# bez wartownika
class Node:
	def __init__(self,val):
		self.next=None
		self.val=val

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


L=List()
L.push(4)
L.push(5)
L.push(3.5)
L.push(2.3)
L.push(3.2)
L.push(2)
L.push(9.6)
L.push(1.21)
L.push(2.11)
L.push(7)
L.push(0)
L.push(1.12)
L.push(1.13)
L.push(1)
L.push(3)

def insertion_sort(L):
	head=L.head
	results=head
	curr=head.next
	results.next=None
	t=head

	while curr:
		start=results
		next=curr.next

		if start.val >curr.val:
			curr.next=start
			results=curr
		else:
			found=False
			while start.next:
				start_next=start.next
				if start.val<=curr.val:
					curr.next=start.next
					start.next=curr
					found=True
				start=start_next
				t=start

				if not found:
					curr.next=None
					start.next=curr
					t=curr
					
		curr=next

	L.head=results
	L.tail=t
	return L  


def bucket_sort(L):
	norm=10

	h=L.head
	l=0
	while h:
		h=h.next
		l=l+1

	T=[List() for _ in range(l)]

	while L.head:
		next=L.head.next
		L.head.next=None
		idx=L.head.val/norm
		T[int(idx*l)].push_node(L.head)
		L.head=next

	for i in range(l):
		if not T[i].is_empty():
			insertion_sort(T[i])


	#tworzymy głowę
	i=0
	while T[i].is_empty():
		i=i+1

	L.head=T[i].head
	L.tail=T[i].tail

	while i<l:
		if T[i].is_empty():
			i=i+1
		else:
			L.tail.next=T[i].head
			L.tail=T[i].tail
			i=i+1

	L.print_list()




bucket_sort(L)

	




