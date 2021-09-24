#Zadanie 1. (problem stacji benzynowych) Pewien podróżnik chce przebyć trasę z punktu A do punktu B. Niestety jego samochód spala dokładnie jeden litr paliwa na jeden kilometr trasy (można powiedzieć, że jedzie czołgiem... znaczenie punktów A i B w ramach obecnej sytuacji geopolitycznej wybierzcie sobie sami). W baku mieści się dokładnie D litrów paliwa. Trasa z A do B to prosta, na której znajdują się stacje benzynowe. Mamy dwa różne zadania (rozwiązywane osobno):
#(1) wyznaczyć trasę, na której tankujemy minimalną liczbę razy.
#(2) wyznaczyć trasę, której koszt jest minimalny (wówczas znamy jeszcze dla każdej stacji cenę za litr paliwa, nie musimy zawsze tankować do pełna).
#(3) Bonus: j.w., ale jeśli na stacji tankujemy, to musimy zatankować do pełna

#1
#tablica A przechowuje nam odległosći od punktu 0-A
#jezeli D jest zbyt mała algorytm powinien zwrócić wartość None
A=[3,5,6,7,8,11]
D=3
B=13
import math

def tank(A,D,B):
	A=A+[B]
	n=len(A)
	T=[0]
	T[0]=A[0]
	i=0
	while i!=(len(A)-1):
		j=i+1
		if A[j]-A[i]>3: return None
		while j<len(A) and A[j]-A[i]<=3:
			j=j+1
		T.append(A[j-1])
		i=j-1
	return(len(T),T)

#print(tank(A,D,B))

#2
A=[(0,0),(3,2),(5,4),(6,1),(7,7),(8,2),(11,2),(12,1),(13,0)]

def problem_tankownaia2(T,D):
	x=0
	n=len(T)
	bak=D
	cost=0

	while x!=n-1:
		min_cost=1e6
		i=x+1
		if T[i][0]-T[x][0]>D:
			return -1
		while i<n and T[x][1]<T[i][1] and T[i][0]-T[x][0]<=D:
			if T[i][1]<=min_cost:
				min_cost=T[i][1]
				y=i
			i=i+1
		
		if T[x][1]>=T[i][1]:
			if bak>T[i][0]-T[x][0]:
				bak=bak-(T[i][0]-T[x][0])
			else:
				cost=cost+(T[i][0]-T[x][0]-bak)*T[x][1]
				bak=0
			x=i
		else:
			cost=cost+(D-bak)*T[x][1]
			bak=D-(T[y][0]-T[x][0])
			x=y

	return ( cost )
		

# test 1
S = [(0,0), (2,4), (4,3), (6,2), (9,3), (11,3), (13,5),(16,4), (18,2), (20,4), (25,0)]
L = 7
#print(problem_tankownaia2(S, L))

# result = 41
# ---------
# test 2
P = [0, 1, 9, 15, 16, 17, 27, 28, 30]
C = [0, 1, 100, 10, 15, 1, 30, 30, 0]
#k=[0]*len(P)
#for i in range(len(P)):
#    k[i]=(P[i],C[i])
L1 = 14
# result: 34
# ---------
# test 3
#S2 = [0, 3, 5, 6, 7, 8, 11, 13]
#C2 = [0, 2, 4, 1, 7, 2, 2, 0]
#L2 = 3

#z=[0]*len(S2)
#for i in range(len(S2)):
#    z[i]=(S2[i],C2[i])

#print(problem_tankownaia2(z, L2))
# result: 17
# ---------   	
# 
#K[i]-ilość piniędzy jaką musimy wydać zatrzymująć sie na tej stacji 
		
def tankowanie_do_pelna_dp(A,D):
	n=len(A)
	#print(F)

	K=[1e6 for i in range(n)]
	K[0]=0
	for i in range(n):
		j=i+1
		while j<n and A[j][0]-A[i][0]<=D:
			K[j]=min(K[j],K[i]+(A[j][0]-A[i][0])*A[j][1])
			j=j+1
	

	if K[n-1]==1e6:
		return -1
	else:
		return K[n-1] 



print(tankowanie_do_pelna_dp(A, 3))