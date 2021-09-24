#. Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie jeden raz. Cyfra wielokrotna to taka, która w liczbie występuje więcej niż jeden raz. Mówimy, że liczba naturalna A jest ładniejsza od liczby naturalnej B jeżeli w liczbie A występuje więcej cyfr jednokrotnych niż w B, a jeżeli cyfr jednokrotnych jest tyle samo to ładniejsza jest ta liczba, która posiada mniej cyfr wielokrotnych. Na przykład: liczba 123 jest ładniejsza od 455, liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są jednakowo ładne.
#Dana jest tablica T zawierająca liczby naturalne. Proszę zaimplementować funkcję: pretty_sort(T) która sortuje elementy tablicy T od najładniejszych do najmniej ładnych. Użyty algorytm powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis algorytmu oraz proszę oszacować jego złożoność czasową.

A=[1444,455,1266,114577,2344,67333,123]

def zlicz_cyfry(x):
	A=[0]*10 #liczby so od 0 do 9
	exp=1
	jednokrotne=0
	wielokrotne=0

	while x//exp>0:
		exp=exp*10
		idx=(x%exp)//(exp//10)
		A[idx]=A[idx]+1


	for i in range(len(A)):
		if A[i]==1:
			jednokrotne=jednokrotne+1
		if A[i]>1:
			wielokrotne=wielokrotne+1

	return ((x,10-jednokrotne,wielokrotne))



def counting_sort(T,key):
	A=[0]*10

	for i in range(len(T)):
		A[T[i][key]]=A[T[i][key]]+1

	for i in range(1,len(A)):
		A[i]=A[i-1]+A[i]

	out=[0]*len(T)
	for i in range(len(T)-1,-1,-1):
		idx=T[i][key]
		A[idx]=A[idx]-1
		out[A[idx]]=T[i]

	for i in range(len(T)):
		T[i]=out[i]



def pretty_sort(T):
	for i in range(len(T)):
		T[i]=zlicz_cyfry(T[i])

	counting_sort(T,2)
	counting_sort(T,1)

	for i in range(len(T)):
		T[i]=T[i][0]

	print(T)
		 
#pretty_sort(A)
#zad.2	Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której podano wzrosty żołnierzy. Żołnierze zostaną ustawieni na placu w szeregu malejąco względem wzrostu. Proszę zaimplementować funkcję: section(T,p,q) która zwróci tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie. Użyty algorytm powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis algorytmu oraz proszę oszacować jego złożoność czasową.
A=[1.7,2.8,2.3,2.5,2.7,3.1,2.6,2.4,1.82,1.99,2.00,2.12,1.33,3.4,2.2]


#O(n+n-p)
#jezeli ma byc posortowana to (p-q+1)log(p-q+1)

def partition(T,start,end):
	pivot=T[end]
	i=start-1

	for j in range(start,end):
		if A[j]>pivot:
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

def section(T,p,q):
	select(A,p,0,len(T)-1)
	select(A,q,p,len(T)-1)

	print(T[p:q+1])

#section(A,0,7)




# Zadanie 3. Proszę zaproponować algorytm, który dla tablicy liczb całkowitych rozstrzyga czy każda liczba z tablicy jest sumą dwóch innych liczb z tablicy. Zaproponowany algorytm powinien być możliwie jak najszybszy. Proszę oszacować jego złożoność obliczeniową

def find_that_all_ok(A):
	curr=0
	

#sorotowanie słownikowe
T=["ania","monika","bl","aga","mama"]


def counting_sort(T,min_l,max_l):
	RES=[0]*(max_l-min_l+1)

	for i in range(len(T)):
		idx=len(T[i])-min_l
		RES[idx]=RES[idx]+1

	for i in range(1,len(RES)):
		RES[i]=RES[i-1]+RES[i]

	out=[0]*len(T)
	
	for i in range(len(T)-1,-1,-1):
		idx=len(T[i])-min_l
		RES[idx]=RES[idx]-1
		idx=RES[idx]
		out[idx]=T[i]
	
	T[0]=out[0]
	K=[]
	idx_last_min_len=0
	for i in range(1,len(T)):
		T[i]=out[i]
		if len(T[idx_last_min_len])<len(T[i]):
			K.append((idx_last_min_len,len(T[idx_last_min_len])))
			idx_last_min_len=i
	K.append((idx_last_min_len,len(T[idx_last_min_len])))
	return K


def counting_sort_for_leter(T,start,key):
	F=[0]*24

	for i in range(start,len(T)):
		idx=ord(T[i][key])-97
		F[idx]=F[idx]+1
	
	for i in range(1,len(F)):
		F[i]=F[i-1]+F[i]
	
	out=[0]*len(T)

	for i in range(len(T)-1,start-1,-1):
		idx=ord(T[i][key])-97
		F[idx]=F[idx]-1
		out[F[idx]+start]=T[i]
	
	for i in range(start,len(T)):
		T[i]=out[i]
	return T



def Radix_sort(T,start,od,do):
	for j in range(do-1,od-1,-1):
		counting_sort_for_leter(T,start,j)
		



def sortowanie(A):
	max_len=0
	min_len=1e6

	for i in range(len(A)):
		min_len=min(len(T[i]),min_len)
		max_len=max(len(T[i]),max_len)

	K=counting_sort(A,min_len,max_len)

	for i in range(len(K)-1,0,-1):
		Radix_sort(T,K[i][0],K[i-1][1],K[i][1])
	Radix_sort(T,0,0,K[0][1])

	return T

print(sortowanie(T))
	
