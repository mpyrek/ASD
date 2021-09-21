
def split_1(L):
	N=L
	while N:
		if N.next:
			if N.val<=N.next.val:
				N=N.next
			
			else:
				head2=N.next
				head2.next=None
	
	return (L,head2)

def merge_sort(L):
	sorted=None

	is_soreted=False

	while not is_soreted:
		is_sorted=True
		while L:
			left,L=split(L)
			right,L=split(L)
			#left right może być puste, ale nasz merge zadziała dobrze 
			if right:
			   is_soreted=False
			x=merge(left,right)
			i=x
			while i.next:
				i=i.next
			i.next=sorted
			sorted=x

		L=sorted

	return sorted
	
	
	


class Node:
	def __init__(self):
		self.next=None
		self.val=None

class List:
	def __init__(self):
		self.head=None
		self.tail=None
	
	def push(self,val):
		N=Node()
		N.val=val
		
		if self.head==None:
			self.head=N
			self.tail=N

		else:
			self.tail.next=N
			self.tail=N

	def pop(self):
		h=self.head
		if h.next==None:
			self.head=None
			self.tail=None
		else:
			while h.next.next:
				h=h.next
		
			self.tail=h
			h.next=None

	def has_one_el(self):
		return self.head==self.tail and self.head!=None

	def is_empty(self):
		return self.head==None
	

	def print_list(self):
		h=self.head
		while h:
			print(h.val)
			h=h.next

	
def split_list(L):
	h=L.head
	count=-1
	
	while h:
		h=h.next
		count=count+1

	H_1=List()
	H_1.head=L.head
	h=L.head

	count=count//2
	while count>0:
		h=h.next
		count=count-1
	
	H_1.tail=h
	H_2=List()
	H_2.head=h.next
	H_1.tail.next=None
	H_2.tail=L.tail

	return ((H_1,H_2))


def merge(L_1,L_2):
	main_list=List()
	if L_1.head.val<=L_2.head.val:
		main_list.head=L_1.head
		main_list.tail=L_1.head
		l=L_1.head.next
		r=L_2.head
	else:
		main_list.head=L_2.head
		main_list.tail=L_2.tail
		l=L_1.head
		r=L_2.head.next		
	
	m_l=main_list.head

	while l and r:
		if l.val<=r.val:
			m_l.next=l
			l=l.next
			m_l=m_l.next
			main_list.tail=m_l
		else:
			m_l.next=r
			r=r.next
			m_l=m_l.next
			main_list.tail=m_l
    
	while l:
		m_l.next=l
		l=l.next
		m_l=m_l.next
		main_list.tail=m_l

	while r:
		m_l.next=r
		r=r.next
		m_l=m_l.next
		main_list.tail=m_l

	return main_list


def split(L):
	if L.has_one_el() or L.is_empty():
		return L
	L_1, L_2 = split_list(L)
	L_1=split(L_1)
	L_2=split(L_2)
	return merge(L_1,L_2)

	



L=List()
L.push(2)
L.push(5)
L.push(3)
L.push(7)
L.push(2)
L.push(8)
L.push(1)
L.push(2)

L=split(L)
L.print_list()

#L.print_list()
#print("pół")
#L_1,L_2 =split_list(L.head)
#L_1.print_list()
#print("Pół")
#L_2.print_list()

#L.print_list()
#L.pop()
#print("pop")
#L.print_list()
#print(L.is_empty())
#print(L.has_one_el())
#L.pop()
#L.print_list()
#print(L.is_empty())
#print(L.has_one_el())
#L.pop()
#print(L.is_empty())
#print(L.has_one_el())