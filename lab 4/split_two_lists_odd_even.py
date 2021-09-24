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

L.push(3)
L.push(5)
L.push(1)
L.push(2)
L.push(3)
L.push(8)
L.push(8)
L.push(2)



def split(L):
	odd=List()
	even=List()


	while L.head:
		k=L.head.next
		if L.head.val%2==1:
			odd.push_node(L.head)

		else:
			even.push_node(L.head)
		L.head.next=None
		L.head=k


	print("nieparzyste: ")
	odd.print_list()
	print("parzyste: ")
	even.print_list()

split(L)