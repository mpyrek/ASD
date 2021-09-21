#Mamy dane n punktów (x, y) w okręgu o promieniu k (liczba naturalna), tzn. 0 <= x2 + y2 <= k, które są w nim równomiernie rozłożone, tzn. prawdopodobieństwo znalezienia punktu na danym obszarze jest proporcjonalne do pola tego obszaru. Napisz algorytm, który w czasie Θ(n) posortuje punkty po ich odległości do punktu (0, 0), tzn. 
#d = sqrt(x2 + y2).
import math
A=[(4,0),(1,1),(3,1),(1,0),(3,3),(1,0),(0,4),(4,0),(0,0)]

def insertion_sort(A):
	l=len(A)
	for j in range(1,l+1):
		key=j-1
		for i in range(0,j):
			if A[i]>A[key]:
				A[i],A[key]=A[key],A[i]



def d(x,y):
	return math.sqrt(pow(x,2)+pow(y,2))

def bucket_sort(A,k):
	n=len(A)

	F=[[] for i in range(n)]

	for el in A:
		x=d(el[0],el[1])/(k+1)
		F[int(x*n)].append(el)


	for el in F:
		print(el)
		insertion_sort(el)
	
	idx=0
	for j in F:
		for i in j:
			A[idx]=i
			idx+=1;

	return A

print(bucket_sort(A,4))