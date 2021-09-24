#Zadanie 1. Proszę zaimplementować algorytm QuickSort (do sortowania tablicy liczb) w sposób iteracyjny (czyli bez korzystania z rekurencji). Należy w tym celu wykorzystać samodzielnie skonstruowany stos. Należy założyć, że dostępne są nastpujące operacje:


class Stack:
	def __init__(self):
		self.tab=[]
		self.elements=0

	def push(self,x):
		self.tab.append(x)
		self.elements=self.elements+1

	def is_empty(self):
		return self.elements==0

	def pop(self):
		self.elements=self.elements-1
		tmp=self.tab.pop()
		return tmp
		

A=[3,-1,5,2,11,3]


def partition(A,start,end):
	x=A[end]
	i=start-1
	for j in range(start,end):
		if A[j]<=x:
			i=i+1
			A[i],A[j]=A[j],A[i]

	A[i+1],A[end]=A[end],A[i+1]
	return i+1


def Quicksort(T,start,end):
	S=Stack()
	S.push((start,end))

	while not S.is_empty():
		x=S.pop()
		if x[0]<x[1]:
			q=partition(T,x[0],x[1])
			S.push((x[0],q-1))
			S.push((q+1,x[1]))
	
	return T

print(Quicksort(A,0,len(A)-1))