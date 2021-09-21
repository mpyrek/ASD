
A=[12,121,11,13,11,22,24,321,54,204]

def Counting_sort(A,exp,k):
	n=len(A)
	out=[0]*n
	B=[0]*k #zakładamy, ze przychodzą liczby od 0 do 9 ~ 10 liczb

	for el in A:
		index=int(el/exp)
		B[index%k]+=1
	for i in range(1,k):
		B[i]+=B[i-1]
	for i in range(n-1,-1,-1):
		index=A[i]/exp
		index=int(index%k)
		B[index]-=1
		out[B[index]]=A[i]
	for i in range(n):
		A[i]=out[i]


def Radix_Sort(A):
	max_el=max(A)
	exp=1
	n=len(A)
	k=10
	while int(max_el//exp>0):
		Counting_sort(A,exp,k)
		exp*=10

Radix_Sort(A)
print(A)