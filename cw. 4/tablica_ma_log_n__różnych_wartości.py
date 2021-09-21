A=[1,3,4,3,6,-2,5,3,1,3,-2,4,-1,5]

#zakłądając że bedziemy mieli dobre wybory pivotów

def partition(A,start,end):
	pivot=A[end]
	i=start-1
	k=start-1

	for j in range(start,end):
		if A[j]<pivot:
			i=i+1
			k=k+1
			A[k],A[i]=A[i],A[k]
			if j!=k:
				A[i],A[j]=A[j],A[i]	#inaczej by był podwójny swap czyli bez zmian
		elif A[j]==pivot:
			k=k+1
			A[j],A[k]=A[k],A[j]

	A[k+1],A[end]=A[end],A[k+1]
	return ((i,k+1))


def quickersort(A,start,end):
	while start<end:
		q=partition(A,start,end)	
		quickersort(A,start,q[0])
		start=q[1]

	print(A)

quickersort(A,0,len(A)-1)