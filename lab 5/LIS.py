#lIS-the Longest Increasing Substring
A=[3,2,1,5,3,7,2,7,8,9]
B=[2,1,4,3,7,6,5]
C=[3,4,-1,5,8,2,3,12,7,9,10]
#złozoność o(nlog(n))

def LIS_n2(T):
	F=[1]*len(T)
	for i in range(1,len(T)):
		for j in range(n):
			if A[j]<A[i] and F[i]<F[j]+1:
				F[i]=F[j]+1
	return max(F)


def print_solution(T,R,i):
	if R[i]!=-1:
		print_solution(T,R,R[i])

	print(T[i],end=' ')

def LIS(T):
	n=len(T)
	F=[1e6 for i in range(n)]
	R=[-1 for i in range(n)]

	F[0]=0
	l=0	

	for i in range(1,n):
		idx=bineary_search(F,T,0,l+1,T[i])
		if idx!=-2:
			if idx+1 > l:
				l = idx+1
			if F[idx+1]==1e6 or T[F[idx+1]]>T[i]:
				F[idx+1]=i
				if F[idx]!=1e6:
					R[i]=F[idx]
	print(l+1)
	print(F)
	print_solution(T,R,F[l])


def bineary_search(tab,T,l,r,x):
	while l<=r:
		mid=(l+r-1)//2
		if T[ tab[mid] ] == x:
			return -2
		elif T[tab[mid]]<x and tab[mid+1]==1e6 or T[tab[mid]]<x and T[tab[mid+1]]>x:
			return mid
		elif mid ==0  and T[tab[mid]]>x:
			return -1
		elif T[tab[mid]]>x:
			return bineary_search(tab,T,l,mid,x)
		else:
			return bineary_search(tab,T,mid+1,r,x)


LIS(A)


		
