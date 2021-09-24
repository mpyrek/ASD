#Problem najdłuższego wspólnego pociciągu dwóch ciągów

A="BDCABA"
B="ABCBDAB"


def LCS(A,B):
	A='0'+A
	B='0'+B
	m=len(A)
	n=len(B)

	F=[[0]*(n) for i in range(m)]
	R=[[0]*n for i in range(m)]
	
	for i in range(1,m):
		for j in range(1,n):
			if A[i] == B[j]:
			   F[i][j]=F[i-1][j-1]+1
			   R[i][j]=0			#0 ozncza że poprzednie pole to i-1, j-1
			elif A[i]!= B[j]:
				F[i][j]=max(F[i][j-1],F[i-1][j])
				if F[i][j-1]>=F[i-1][j]:
					R[i][j]=1
				else:
					R[i][j]=2
	print_LCS(R,A,m-1,n-1)
	return(F[m-1][n-1])

def print_LCS(b,X,i,j):
	if i==0 or j==0:
		return
	if b[i][j]==0:
		print_LCS(b,X,i-1,j-1)
		print(X[i],end='')
	elif b[i][j]==1:
		print_LCS(b,X,i,j-1)
	else: print_LCS(b,X,i-1,j)

LCS(A,B)