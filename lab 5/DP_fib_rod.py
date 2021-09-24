#fib(0)=1 fib(1)=1
import math

def fib(n):
	if n<=1:
		return 1
	return fib(n-1)+fib(n-2)

def fibDP(n):
	F=[1]*(n+1)
	for i in range(2,n+1):
		F[i]=F[i-1]+F[i-2]
	return F[n]
			
def fib_better_DP(n):
	if n<=1:
		return 1
	F1=1
	F2=1
	for i in range(2,n+1):
		Fi=F1+F2
		F1,F2=F2,Fi
	return Fi

N=20
F=[0]*N
F[0]=1
F[1]=1

def fib_mem(n):
	if F[n]>0:
		return F[n]
	F[n]=fib_mem(n-1)+fib_mem(n-2)
	return F[n]

#print(fib_mem(5))

#pręt


p=(0,1,5,8,9,10,17,17,20,24,30)

def cut_rod(p,n):
	if n==0:
		return 0
	q=-1000
	for i in range(1,n+1):
		q=max(q,p[i]+cut_rod(p,n-i))
	return q

n=len(p)
Q=[0]*(n+1)

#metoda zstępująca ze spamiętywaniem
def memoized_cut_rod(p,n,Q):
	if Q[n]>0:
		return Q[n]
	if n==0:
		q=0
	else:
		q=-math.inf
		for i in range(1,n+1):
			q=max(q,p[i]+memoized_cut_rod(p,n-i,Q))
	Q[n]=q
	return q

# metoda wstępująca
def bottom_up_cut_rod(p,n):
	r=[0]*(n+1)
	for j in range(1,n+1):
		q=-math.inf
		for i in range(1,j+1):
			q=max(q,p[i]+r[j-i])
		r[j]=q
	print(r)
	return r[n]

def extended_botom_rod(p,n):
	r=[0]*(n+1)
	s=[-1]*(n+1)

	for j in range(1,n+1):
		q=-math.inf
		for i in range(1,j+1):
			if q < p[i]+r[j-i]:
				q=max(q,p[i]+r[j-i])
				s[j]=i
		r[j]=q
	print(r)
	return (r[n],s)



print(p)
#print(cut_rod(p,8))
#print(memoized_cut_rod(p,8,Q))
#print(Q)
#print(bottom_up_cut_rod(p,8))
print(extended_botom_rod(p,10))