#Dana jest tablica  A[N] oraz liczba x. Czy istnieją indeksy i i j, takie że A[i]+A[j]=x // O(n)

P=[-4,-2,-2,0,2,4,6]
B=[2,6,4,5,3,8,5,76,1,33]
# Zadanie 3. Proszę zaproponować algorytm, który dla tablicy liczb całkowitych rozstrzyga czy każda liczba z tablicy jest sumą dwóch innych liczb z tablicy. Zaproponowany
# algorytm powinien być możliwie jak najszybszy. Proszę oszacować jego złożoność obliczeniowa

#Radix sort dla liczb całkowitych(można jakim kolwiek sortowanie nawet O(n^2))
def Counting_sort(A,exp,k):
	n=len(A)
	out=[0]*n
	B=[0]*(k*2-1) #zakładamy, ze przychodzą liczby od -9 do 9 ~ 10 liczb
	for el in A:
		index=int(el/exp)
		if(index>=0):
			B[(index%k)+9]+=1
		else:
			B[(index%k)]+=1
	for i in range(1,len(B)):
		B[i]+=B[i-1]
	for i in range(n-1,-1,-1):
		index=A[i]/exp
		if A[i]>=0:
			index+=9
			index=int(index%(2*k))
			B[index]-=1
			out[B[index]]=A[i]
		else: 
			index=int(index%k)
			B[index]-=1
			out[B[index]]=A[i]
	for i in range(n):
		A[i]=out[i]


def Radix_Sort(A):
	max_el=max(A)
	min_el=min(A)
	max_el=max(abs(max_el),abs(min_el))
	max_count_of_digits=0
	exp=1
	n=len(A)
	k=10
	while int(max_el//exp>0):
		Counting_sort(A,exp,k)
		exp*=n
	return A


def exist(Z,t):
	x=Z[t]
	i=0
	N=len(Z)
	j=N-1
	if t==0:
	   i+=1
	if t==N-1:
		j-=1
	x-=(Z[i]+Z[j])
	while x!=0 and i+1!=j:
		if x>0:
			x+=Z[i]
			if i+1==t: i+=1
			if i+1==j: return False
			i+=1
			x-=Z[i]
		elif x<0:
			x+=Z[j]
			if j-1==t: j-=1
			if j-1==i: return False
			j-=1
			x-=Z[j]

	if x==0: return True
	return False


def prawda(A):
	A=Radix_Sort(A)
	for t in range(len(A)):
		if exist(A,t)==False: return False
	return True

print(prawda(P))