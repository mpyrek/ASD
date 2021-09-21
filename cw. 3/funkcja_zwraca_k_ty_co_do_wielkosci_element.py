

#zwraca idx
def partition(A,start,end):
	pivot=A[end]
	i=start-1
	for j in range(start,end):
		if A[j]<=pivot:
			i=i+1
			A[i],A[j]=A[j],A[i]

	A[i+1],A[end]=A[end],A[i+1]
	return i+1

#zwaraca el nie idx
def Select(A,start,end,k):
	if start==end:
		return A[end]
	q=partition(A,start,end)		

	if q==k:
		return A[q]
	if k<q:
		return Select(A,start,q-1,k)
	else:
		return Select(A,q+1,end,k)

A=[1,5,2,3,-2,4,5]
print(Select(A,0,len(A)-1,3))
print(A)

