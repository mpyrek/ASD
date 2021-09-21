T=[1,2,3,2,2,3,4,5,7,3,4,5,1,2]

def find_seried(T,i):
    if i==0:
        while i+1<len(T) and T[i]<=T[i+1]:
            i=i+1
    j=i+1
    while j+1<len(T) and T[j]<=T[j+1]:
        j=j+1
    
    merge(T,0,i+1,j)
    if j!=len(T):
        find_seried(T,j)
    else:
        return T




def merge(T,p,q,r):
    A=T[p:q]
    B=T[q:r+1]
    i=0
    p=0
    q=0
    while p<len(A) and q<len(B):
        if A[p]<=B[q]:
            T[i]=A[p]
            p=p+1
        else:
            T[i]=B[q]
            q=q+1
        i=i+1

    while p<len(A):
        T[i]=A[p]
        p=p+1
        i=i+1
    while q<len(B):
        T[i]=B[q]
        q=q+1
        i=i+1            
            
            

find_seried(T,0)
print(T)





#listy 


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


L=List()

L.push(3)
L.push(4)
L.push(7)
L.push(1)
L.push(2)
L.push(3)
L.push(4)
L.push(2)
L.push(5)

def split1(N):
    if not N:
        return ((None,None))
    H_1=N
    while N.next and N.val<=N.next.val:
        N=N.next
    
    H_2=N.next
    N.next=None
    return ((H_1,H_2))

def merge1(l,r):
    if l and r:
        if l.val<=r.val:
            mian_list=l
            l=l.next
        else:
            mian_list=r
            r=r.next
        head=mian_list
    else:
        if l:
            return l
        else:
            return r

    while l and r:
        if l.val<=r.val:
            mian_list.next=l
            l=l.next
        else:
            mian_list.next=r
            r=r.next
        mian_list=mian_list.next 
    
    if l:
        mian_list.next=l
    if r:
        mian_list.next=r        
    
    return head


def merge_sort1(head):
    is_soreted=False
    sorted=None
    while head!=None and not is_soreted:
        is_soreted=True
        l,head=split1(head)
        r,head=split1(head)
        if head:
            is_soreted=False
        #else:
        #    r=head
        x=merge1(l,r)
        i=x
        while i.next:
            i=i.next
        i.next=head
        sorted=x
        head=sorted
    return sorted


x=merge_sort1(L.head)
while x:
    print(x.val)
    x=x.next