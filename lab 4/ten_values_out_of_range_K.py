#5. Masz daną tablicę zawierającą n (n >= 11) liczb naturalnych w zakresie [0, k]. Zamieniono 10 liczb z tej tablicy na losowe liczby spoza tego zakresu (np. dużo większe lub ujemne). Napisz algorytm, który posortuje tablicę w czasie O(n).
k=12

T=[4, 4 , 7, -30, 12, 102,33,11,11,1,2,3,-1,-4,3,2,22,7,4,5,5,25,6,4,55,11,12,11,-10,3,44,5]


def insertion_sort(A,start,end):
	for i in range(start+1,end):
		key=A[i]
		j=i-1
		while j>=start and A[j]>key:
			A[j+1]=A[j]
			j=j-1
		A[j+1]=key


def counting_sort(A,k,start,end):
	n=end-start
	F=[0 for i in range(k+1)]
	out=[0 for i in range(n)]

	for el in A[start:end]:
		F[el]=F[el]+1

	for i in range(1,len(F)):
		F[i]=F[i-1]+F[i]

	for i in range(end-1,start-1,-1):
		idx=A[i]
		F[idx]=F[idx]-1
		out[F[idx]]=A[i]

	for i in range(start,end):
		A[i]=out[i-start]


def find_outisde_k(A,k):
	end=len(A)-1
	start=0
	i=0

	while i<end:
		if A[i]<0:
			if i!=start: 
				A[i],A[start]=A[start],A[i]
				i=i-1
			start=start+1
		elif A[i]>k:
			A[i],A[end]=A[end],A[i]
			end=end-1
			i=i-1
		i=i+1

	
	counting_sort(A,k,start,end+1)
	insertion_sort(A,0,start)
	insertion_sort(A,end+1,len(A))

	print(A)

	

find_outisde_k(T,k)

