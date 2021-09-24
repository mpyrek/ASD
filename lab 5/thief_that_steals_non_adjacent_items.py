#f(i)- największy możliwy zysk dla i elementu  bez niego(i-tego el nie bierzemy)

A=[20,7,2,11,3]

F=[0]*(len(A)+1)
F[0]=0
F[1]=A[0]
F[2]=max(A[0],A[1])

def thief(A,n):
	for i in range(3,n+1):
		F[i]=max(A[i-1]+F[i-2],F[i-1])
	return F[n]

print(thief(A,len(A)))