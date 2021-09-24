#Monika Pyrek
# Zadanie wykonałam posługując się funkcją przedstawioną na wykładzie jednak dla wygody zaimplementowaną iteracyjnie. Podczas zliczania długości ścieżki, zapisuję również idx, potrzebne do odtworzenia rozwiązania.W funkcji print_solution zmienne end_of_1,end_of_2(end_of_2<end_of_1) przetrzymują wartości i,j, dzięki których wiemy, że aktualnie jesteśmy na pozycji F(i,j). Rozwiązanie będę odtwarzać w następujący sposób:
# 1) jeżeli i<F(i,j)[1]<j => T1.append(T[F(i,j)[1]]) i kontynuujemy z pewnością, żę i<j
# 2) jeżeli F(i,j)[1]<i<j => T1.append(T[F(i,j)][1]) i w tym momencie musimy zmienić miejscami tablice T1,T2 oraz "i" i "j", aby utrzymać konwencję, że i < j (end_of_2<end_of_1) 
# złożoność czasowa O(n^2), złożoność pamięciowa O(n^2)  [T1 i T2 alokują w sumie O(n) dodatkowej pamięci]



from math import *

C = [["Wrocław", 0, 2], ["Warszawa",4,3], ["Gdańsk", 2,4], ["Kraków",3,1]]

def distance(x,y):
  p=sqrt(pow(x[1]-y[1],2)+pow(x[2]-y[2],2))
  return p


def print_solution(T,F,T1,end_of_1,T2,end_of_2):
    #wypisywanie rozwiązania
	if end_of_1==0 and end_of_2==0:
		for i in range(len(T1)-1,-1,-1):
			print(T1[i],end=', ')
		for i in range(len(T2)-1):
			print(T2[i],end=', ')
		print(T2[len(T2)-1])

	idx=F[end_of_2][end_of_1][1]
	if idx < end_of_1 and idx>=end_of_2:
		T1.append(T[idx][0])
		print_solution(T,F,T1,idx,T2,end_of_2)
	elif idx<end_of_1 and idx<end_of_2 and end_of_2==end_of_1-1:
		T1.append(T[idx][0])
		print_solution(T,F,T2,end_of_2,T1,idx)

def bitonicTSP( C ):
  """miejsce na Twoją implementację!"""
  C.sort(key=lambda x: x[1])

  n=len(C)
  F=[[[1e6,0] for i in range(n)] for j in range(n)]
  F[0][0][0]=0
  F[0][1][0]=distance(C[0],C[1])
  F[0][1][1]=0

  for i in range(0,n):
    for j in range(i+1,n):
      if i==j-1:
        for k in range(0,j):	#do j-1
          if F[i][j][0]>(F[k][j-1][0]+distance(C[k],C[j])):
            F[i][j][0]=F[k][j-1][0]+distance(C[k],C[j])
            F[i][j][1]=k

      elif i<j-1:
        F[i][j][0]=F[i][j-1][0]+distance(C[j-1],C[j])
        F[i][j][1]=j-1

  for i in range(n-1):
    if F[n-1][n-1][0]>F[i][n-1][0]+distance(C[i],C[n-1]):
      F[n-1][n-1][0]=F[i][n-1][0]+distance(C[i],C[n-1])		
      F[n-1][n-1][1]=i

  T1=[C[n-1][0]]
  T2=[C[F[n-1][n-1][1]][0]]

  print_solution(C,F,T1,n-1,T2,F[n-1][n-1][1])
  print(F[n-1][n-1][0])

  pass
  
  
  
bitonicTSP( C )
