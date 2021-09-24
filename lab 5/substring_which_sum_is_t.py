#Dany jest zbiór n liczb repreezentowany jako tablica A[n]. Wykorzystując programowanie dynamiczne oparte na f(x) napisać algorytm, który sprawdza, czy da się wybrać podzbiów liczb dokładnie o zadanej sumie t
#f(x)=1,A[o].,,,A[i] da się ułożyć w x(liczby A[0],...A[i] sumują sie do x)
#f(x)-2 jeśli sie nie da lub po prostu -1


A=[2,2,3,2]

def sum_Af(A,x):
	n=len(A)

	W=[[0]*n for i in range(x+1)]
	
	for i in range(x+1):
		for j in range(len(A)):
			if i==A[j]:
    				 W[i][j]=1
			#żeby nie brać po 2 razy tej samej liczby musimy zobaczyć czy w polu wyżej juz była możliwosoć uzyskania liczby i-A[j]
			elif i-A[j]>=0 and j>=1 and W[i-A[j]][j-1]==1:
    				 W[i][j]=1
			elif j>=1 and W[i][j-1]==1:
    				 W[i][j]=1
			#else: W[i][j]=2

	if W[x][n-1]==1:
    		 return True
	return False

#print(sum_Af(A,7))

#złożoność O(t*n)

#f(i,j)-sume j mozna otrzymac z prośród od 0 do i elementów
def sum(A,x):
	F=[[0]*(x+1) for i in range(len(A))]

	# warunek początkowy: f(i,j)=1 if A[i]==j
	for i in range(len(A)):
		if A[i]<x:
			F[i][A[i]] = 1

	for i in range(1,len(A)):
		for j in range(x+1):
			#jeżeli daną sume mozna było osiągnąc z i-1 el to z i el też można 
			if F[i-1][j]==1:
				F[i][j]=1				
			#jezeli F[i-1][j-A[i]] pozwala osiągną sume mniejszą od A[i] to dodanie A[i] pozwlaa osiągnąc sume j
			elif j-A[i]>=0 and F[i-1][j-A[i]]==1:
				F[i][j]=1

	if F[len(A)-1][x]==1:
		return True
	else:
		return False
			 


print(sum(A,6))