#średnia nlogn pesymistyczna n^2, niestabilny

T=[-2,1,4,2,22,-10,9,2]


def partition(A,p,r):
	x=A[r]
	i=p-1
	
	for j in range(p,r):
		if A[j]<=x:
			i=i+1
			A[j],A[i]=A[i],A[j]
		
	A[i+1],A[r]=A[r],A[i+1]
	return i+1


def quicksort(T,start,end):
	while start<end:
		q=partition(T,start,end)
		if q-start<end-q:
			quicksort(T,start,q-1)
			start=q+1
		else:
			quicksort(T,q+1,end)
			end=q-1
	
	return T

print(quicksort(T,0,len(T)-1))
