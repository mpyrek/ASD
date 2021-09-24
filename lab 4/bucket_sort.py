import math

B=[5,2,3,6,1,2,3,4,9,6,7,4,11]


def insertion_sort(A):
	l=len(A)
	for j in range(1,l+1):
		key=j-1
		for i in range(0,j):
			if A[i]>A[key]:
				A[i],A[key]=A[key],A[i]

def bucket_sort(G):
	n=len(G)
	norm=max(G)
	F=[[] for i in range(n)]
	for el in G:
		x=el/norm
		F[int(x*n)].append(el)
	for el in F:
		insertion_sort(el)
	idx=0
	for j in F:
		for i in j:
			G[idx]=i
			idx+=1

print(B)
bucket_sort(B)
print(B)
	