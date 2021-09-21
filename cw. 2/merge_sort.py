A=[2,5,7,3,5,3,2]
B=[1,7,4,5,3,9,2,8]
C=[2,7,4,5,3,5,2]
L=[1,6,12,3,54,21,34,5,8]


def mergesort(A):
	if len(A) > 1:
		mid=len(A)//2
		L=A[:mid]
		R=A[mid:]

		mergesort(L)
		mergesort(R)


		i=j=k=0
		while i<len(L) and j<len(R):
			if L[i]<=R[j]:
				A[k]=L[i]
				i=i+1
			else:
				A[k]=R[j]
				j=j+1
			k=k+1
	
		while i<len(L):
			A[k]=L[i]
			i=i+1
			k=k+1
		while j<len(R):
			A[k]=R[j]
			k=k+1
			j=j+1

		return A

#print(mergesort(D))

#program scalający k posortowanych tablic:

T=[[1,3,4,5],[2,8],[1,3,4],[2]]


def merge_2_tab(A):
	k=len(A)
	L=[el for el in A[:k//2]]
	R=[el for el in A[k//2:]]

	if len(L)>1: merge_2_tab(L)
	if len(R)>1: merge_2_tab(R)

	i=j=k=0
	while i<len(L) and j<len(R):
		if L[i]<=R[j]:
			A[k]=L[i]
			i=i+1
		else:
			A[k]=R[j]
			j=j+1
		k=k+1
	
	if i<len(L):
		A[k]=L[i]
		i=i+1
		k=k+1
	if j<len(R):
		A[k]=R[j]
		k=k+1
		j=j+1
	return A 
	

def merge3(A,n):
	A=merge_2_tab(A)
	K=[None]*n

	for i in range(n):
		K[i]=A[0][0]
		if len(A[0])>1:
			A[0]=A[0][1:len(A[0])]
		else: A=A[1:]
		merge_2_tab(A)
	print(K)

#merge3(T,10)

#Proszę zaproponować strukturę przechowującą liczby naturalne, w której operacje: Insert i GetMedian mają złożoność O(log(n)). Proszę zaimplementować w/w operacje.

class n_numbers:
	def __init__(self,A):
		self.A=A
		self.n=len(A)
	





#Proszę zaimplementować algorytm zliczający liczbę inwersji w tablicy. (Inwersja to para indeksów i, j taka, że i < j oraz T[i] > T[j])


#count=0
def merge_sort_count(A):
	count=0
	n=len(A)
	if n > 1:
		mid = n//2
		L=A[:mid]
		R=A[mid:]

		merge_sort_count(R)
		merge_sort_count(L)

		i=j=k=0
		while i<len(L) and j<len(R):
			if L[i]<=R[j]:
				A[k]=L[i]
				i=i+1
			else:
				A[k]=R[j]
				j=j+1
				#jeżeli dany el musi sie zamienic z lewym to niee tylko posiada inwerse z tym el ale z wszystkimi co stoją przed nim 
				count=count+len(L)-i
			k=k+1
	
		while i<len(L):
			A[k]=L[i]
			i=i+1
			k=k+1
		
		while j<len(R):
			A[k]=R[j]
			k=k+1
			j=j+1
	
	return count


def split(L):
	n=len(L)
	mid = n//2
	L=A[:mid]
	R=A[mid:]
	
	return L,R

def merge(L,start,mid,end):
	count=0
	i=start
	j=mid+1
	T=[]
	while i<=mid and j<=end:
		if L[i]<=L[j]:
			T.append(L[i])
			i=i+1
		else:
			T.append(L[j])
			j=j+1
			#jeżeli dany el musi sie zamienic z lewym to niee tylko posiada inwerse z tym el ale z wszystkimi co stoją przed nim 
			count=count+mid-i+1
	
	while i<=mid:
		T.append(L[i])
		i=i+1
		
	while j<=end:
		T.append(L[j])
		j=j+1

	s=end-start+1
	i=0
	while i<s:
		L[start + i] = T[i]
		i += 1
	
	return count


def merge22(L,start,end):
	count =0

	if start!=end:
		mid=(start+end)//2
		count=count+merge22(L,start,mid)
		count=count+merge22(L,mid+1,end)
		count=count+merge(L,start,mid,end)
	return count
	


D=[4,3,2]
T=[1,2,1,4,3,1]
#print(merge_sort_count(L))
#print(merge22(T,0,len(T)-1))



#najlepszy merge sort


def OK_Merge7(tab, l, div, r,temp):
    for i in range(l, r + 1):
		temp[i] = tab[i]

	l_i = l
	r_i = div + 1
	c_i = l

	while l_i <= div and r_i <= r:
		if temp[l_i] <= temp[r_i]:
			tab[c_i] = temp[l_i]
			l_i += 1

		else:
			tab[c_i] = temp[r_i]
			r_i += 1

		c_i += 1

	while l_i <= div:
		tab[c_i] = temp[l_i]
		c_i += 1
		l_i += 1



def merge7(tab, l, r,temp):
	div = (l + r) // 2

	if l < r:
		merge7(tab, l, div,temp)
		merge7(tab, div + 1, r,temp)
		OK_Merge7(tab, l, div, r,temp)


def merge_sort7(T):
	temp = []
	for i in range(len(T)):
		temp.append(0)

	merge7(T, 0, len(T) - 1,temp)
	return T


print(merge_sort7(T))