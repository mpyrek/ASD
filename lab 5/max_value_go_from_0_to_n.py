end=None

class Field:
	def __init__(self,v,l_j,s_j):
		self.v=v
		self.l=l_j
		self.s=s_j

def licz_max(A):
	n=len(A)
	F=[-1]*n
	F[0]=A[0].v
	
	for i in range(len(A)):
		if F[i]==-1: continue
		if i+A[i].l<n:
			F[i+A[i].l]=max(F[i+A[i].l],F[i]+A[i+A[i].l].v)
		if i+A[i].s<n:
			F[i+A[i].s]=max(F[i+A[i].s],F[i]+A[i+A[i].s].v)
	return F[n-1]

A=[0]*7

A[0]=Field(3,2,3)
A[1]=Field(1,1,2)
A[2]=Field(4,2,3)
A[3]=Field(5,1,3)
A[4]=Field(6,1,1)
A[5]=Field(2,1,3)
A[6]=Field(3,1,1)

print(licz_max(A))
