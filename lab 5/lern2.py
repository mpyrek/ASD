#*Zadanie 1. (problem sumy podzbioru) Dana jest tablica n liczb A. Proszę podać i zaimplementować
#	algorytm, który sprawdza, czy da się wybrać podzbiór liczb z A, które sumują się do zadanej wartości T.

X=[2,1,5,2,3,5,2,2,3,4,1,3,2,3,1,1,2,3,2]
B=[2,4,6,3]

def PS(A,T,idx):
	print(T)
	if T==0: 
		return True
	if T<0 or idx>=len(A): 
		return False
	for i in range(idx,len(A)):
		if (PS(A,T-A[i],i+1)): return True
	return False



def PS_DP(A,T):
	s=sum(A)
	n=len(A)
	if(s<T): return False
	F=[0]*len(A)
	for i in range(0,n):
		F[i]=[0]*(T+1)
	for i in range(A[0],T+1): F[0][i]=A[0]
	for i in range(1,n):
		for w in range(1,T+1):
			F[i][w]=F[i-1][w]
			if w>=A[i]:
				F[i][w]=max(F[i][w],F[i-1][w-A[i]]+A[i])
	print(F)
	if F[n-1][T]==T:return True
	return False





def PS_DP2(A,T):
	s=sum(A)
	n=len(A)
	if(s<T): return False
	F=[0]*len(A)
	for i in range(0,n):
		F[i]=[0]*(T+1)
	for i in range(n):
		if A[i]<=T:
			x=A[i]
			F[i][x]=1
	for i in range(1,n):
		for w in range(1,T+1):
			if F[i][w]!=1: F[i][w]=F[i-1][w]
			if w>=A[i]:
				if F[i-1][w-A[i]]==1:
					F[i][w]=1
	print(F)
	if F[n-1][T]==1:return True
	return False

#print(PS_DP2(B,3))
#print(PS_DP(B,3))


#*Zadanie 1. (problem sumy podzbioru) Dana jest tablica n liczb A. Proszę podać i zaimplementować
#	algorytm, który sprawdza, czy da się wybrać podciąg liczb z A, które sumują się do zadanej wartości T.

def Substring(A,T,l,r):
	if T==0: return True
	if r==len(A) and (T>0 or l==len(A)): return False
	if T>0:
		return Substring(A,T-A[r],l,r+1)
	if T<0:
		return Substring(A,T+A[l],l+1,r)


def Substring2(A,T):
	n=len(A)
	r=0
	l=0
	while r!=n or l!=n:
		if r==n and T>0: break

		if T>0:
			T-=A[r]
			r+=1
		elif T<0:
			T+=A[l]
			l+=1
		else:
			break
	if T==0:
	   return True
	return False

print(Substring(B,7,0,0))
print(Substring2(B,7))