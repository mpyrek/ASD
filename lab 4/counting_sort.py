import math

B=[1,6,9,1,1,3,6,6,4,5,3,4,5,6,2,1]

def counting_sort(A):
	n=len(A)
	F=[0]*(max(A)+1)
	for el in A:
		F[el]+=1
	for i in range(1,max(A)+1):
		F[i]+=F[i-1]
	out=[0]*n
	print(n)
	for j in range(n-1,-1,-1):
		el=A[j]
		F[el]-=1
		out[F[el]]=el
	print(out)
	for i in range(n-1,-1,-1):
		A[i]=out[i]

C=[123,456,183]

def radix_sort(A):
	A=A%10

radix_sort(C)
print(C)