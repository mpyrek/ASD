
class Node:
	def __init__(self,x):
		self.next=None
		self.val=x

class Queue:
	def __init__(self):
		self.Q=Node(None)
		self.tail=Node(None)

	def enqueue(self,x):
		N=Node(x)
		if self.Q.next==None:
			N.next=self.Q.next
			self.Q.next=N
			self.tail.next=N
		else:
			self.tail.next.next=N
			self.tail.next=N
		
	def dequeue(self):
		z=self.Q.next.val
		self.Q.next=self.Q.next.next
		return z

	def is_epmty(self):
		return self.Q.next==None


def captain(M,P,s):
	Parent=[(None,0,s)]
	Q=Queue()
	l=len(M[0])
	h=len(M)

	Q.enqueue(Parent[0])
	T=[[False]*len(M[0]) for i in range(len(M))]
	
	while Q.is_epmty() == False:
		u=Q.dequeue()
		
		row=u[2][0]
		col=u[2][1]
		 
		if row+1<h and T[row+1][col]==False and M[row+1][col]>=P:
			T[row+1][col]=True
			Q.enqueue(([row,col],u[2][1]+1,[row+1,col]))
			Parent=Parent+[([row,col],u[2][1]+1,[row+1,col])]	
		if row-1>=0 and T[row-1][col]==False and M[row-1][col]>=P:
			T[row-1][col]=True
			Q.enqueue(([row,col],u[2][1]+1,[row-1,col]))
			Parent=Parent+[([row,col],u[2][1]+1,[row-1,col])]
		if col+1<l and T[row][col+1]==False and M[row][col+1]>=P:
			T[row][col+1]=True
			Q.enqueue(([row,col],u[2][1]+1,[row,col+1]))
			Parent=Parent+[([row,col],u[2][1]+1,[row,col+1])]
		if col-1>=0 and T[row][col-1]==False and M[row][col-1]>=P:
			T[row][col-1]=True
			Q.enqueue(([row,col],u[2][1]+1,[row,col-1]))
			Parent=Parent+[([row,col],u[2][1]+1,[row,col-1])]
	print(Parent)




M=[[1,2,3,2],[2,3,1,2],[3,3,3,3]]
captain(M,2,[0,0])