from random import shuffle

def counting_sort1(A,key):
	
	F=[0]*(key)

	for el in A:
		F[el%key]=F[el%key]+1

	for i in range(1,len(F)):
		F[i]=F[i]+F[i-1]


	out=[0]*len(A)

	for i in range(len(A)-1,-1,-1):
		idx=A[i]%key
		F[idx]=F[idx]-1
		out[F[idx]]=A[i]

	for i in range(len(A)):
		A[i]=out[i]

	return A




def counting_sort2(A,key):
	F=[0]*(key)

	for el in A:
		F[el//key]=F[el//key]+1

	for i in range(1,len(F)):
		F[i]=F[i]+F[i-1]


	out=[0]*len(A)
	for i in range(len(A)-1,-1,-1):
		idx=A[i]//key
		F[idx]=F[idx]-1
		out[F[idx]]=A[i]

	for i in range(len(A)):
		A[i]=out[i]

	return A


def radix_sort():
	n=9
	A=[0]*pow(n,2)
	for i in range(0,pow(n,2)):
		A[i]=i

	shuffle(A)
	print(A)
	counting_sort1(A,n)
	counting_sort2(A,n)
	print(A)

radix_sort()