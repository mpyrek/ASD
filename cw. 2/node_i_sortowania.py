
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

	def is_empty(self):
		return self.head==None

	def has_one_el(self):
		return self.head==self.tail and self.head!=None

	def print_list(self):
		h=self.head
		while h:
			print(h.val)
			h=h.next
L=List()
L.push(2)
L.push(8)
L.push(3)
L.push(4)
L.push(1)
L.push(9)

#L.print_list()


def split_in_half(L):
	h=L.head
	count=0
	while h:
		count=count+1
		h=h.next
	
	count=count//2

	new_tail_left=L.head
	new_head_right=L.head

	while count!=0:
		new_tail_left = new_head_right
		new_head_right=new_head_right.next
		count=count-1

	new_tail_left.next=None

	R=List()
	R.head=new_head_right
	R.tail=L.tail
	L.tail=new_tail_left

	return(L,R)



def merge(L,R):
	if R.is_empty():
		return L
	if L.is_empty():
		return R
	
	main_list=List()

	l=Node(None)
	r=Node(None)
	m_l=Node(None)

	if L.head.val<=R.head.val:
		main_list.head=L.head
		m_l=main_list.head
		main_list.tail=m_l
		l=L.head.next
		r=R.head
	else:
		main_list.head=R.head
		main_list.tail=m_l
		m_l=main_list.head
		l=L.head
		r=R.head.next

	while l!=None and r!=None:
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

	while l!=None:
		m_l.next=l
		l=l.next
		m_l=m_l.next
		main_list.tail=m_l
	while r!=None:
		m_l.next=r
		r=r.next
		m_l=m_l.next
		main_list.tail=m_l
	
	return main_list


def merge_sort(L):

	if L.is_empty() or L.has_one_el(): 
		return L
	left,right=split_in_half(L)
	left=merge_sort(left)
	right=merge_sort(right)
	
	return merge(left,right)

x=merge_sort(L)
x.print_list()