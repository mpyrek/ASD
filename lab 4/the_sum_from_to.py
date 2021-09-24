#suma od do 

A=[1,-100,2,3,4,30,22,1,449,55]

def partition(T,start,end):
	pivot=T[end]
	i=start-1

	for j in range(start,end):
		if A[j]<=pivot:
			i=i+1
			A[j],A[i]=A[i],A[j]

	A[i+1],A[end]=A[end],A[i+1]
	return i+1

def select(A,k,start,end):
	if start==end:
		return A[end]
	q=partition(A,start,end)

	if k==q:
		return A[k]
	if k<q:
		return select(A,k,start,q-1)
	else:
		return select(A,k,q+1,end)

print(A)
x=select(A,2,0,len(A)-1)
print(x)
print(A)
y=select(A,5,3,len(A)-1)
print(y)
print(A)

count=0
for i in range(2,6):
	count+=A[i]
	print(A[i])

print(count)