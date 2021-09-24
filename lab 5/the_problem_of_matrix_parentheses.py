p=[30,35,15,5,10,20,25]
import math
#do linijki 21 mnożenie 2 macierzy
class Matric:
	def __init__(self,X,rows,columns):
		self.X=X
		self.rows=rows
		self.columns=columns

#A=Matric(tab1[2][3],2,3)
#B=Matric(tab2[3][5],3,5)
#print(A.columns)
def matrix_mulityply(A,B):
	if A.columns!=B.rows: return False
	else:
		C=Matrix(A.rows,B.columns)
		for r in range(A.rows):
			for c in range(B.columns):
				C[r][c]=0
				for k in range(A.columns):
					C[r][c]=C[r][c]+A[r][k]*B[k][c]

def matrix_parentheses(p):
	n=len(p)-1 #ilość macierzy
	m=[[-1]*(n) for i in range(n)]
	s=[[-1]*(n) for i in range(n)]
	
	for i in range(n): m[i][i]=0
	
	for l in range(2,n+1):
		for i in range(0,n-l+1):
			j=i+l-1
			m[i][j]=1e6
			for k in range(i,j):
				q=m[i][k]+m[k+1][j]+p[i]*p[k+1]*p[j+1]
				if q<m[i][j]:
					m[i][j]=q
					s[i][j]=k
	print(m)
	print(print_solution(s,0,len(p)-2))
	return m[0][n-1]

def print_solution(s,i,j):
	if j==i:
		print("A",i,"x","A",i+1,end='')
	else:
	   print("(",end='')
	   print_solution(s,i,s[i][j])
	   print_solution(s,s[i][j]+1,j)
	   print(")",end='')


print(matrix_parentheses(p))



def matrix_parentheses2(p):
	#tworzymy sobie nową tablice m[1..n,1..n]<-trzymająca optymalną liczbe podziałów dla macierzy nxn
	#tablica s[1..n-1,2...n]<-trzymającą liczbe k dla którego podizał 1-k, k+1-n ma najoptymalniejszą liczbe podziałów
	#(zaczynamy od 2 i konczymy na n-1 bo dla macierzy o wymiaracg 1,1 2,2, n,n  liczba k nie istnieje-szukamy podizłu 1-6, zaczynając od podziału 1,2 2,3 3,4 itd. {trójkąt})
	n=len(p)-1 #liczba naszych macierzy
	m=[[0]*(n-i+1) for i in range(1,n+1)] # powstaje nam tablica 6x6 (1,2,3..6 x 6,5..,3,2,1) (tablica n na n)
	s=[[-1]*(n-i) for i in range(1,n)] #potrzebna nam jest tylko 1-n-1  i 2- n (tablica n na n)
	#for i in range(n):
		#m[i][i]=0
	for l in range(2,n+1):
		for i in range(0,n-l+1):
			j=i+l-1
			#print(i,j)
			m[i][j-i]=1e6
			for k in range(i,j):
				q=m[i][k-i]+m[i+1][j-k-1]+p[i]*p[k+1]*p[j+1]
				if q<m[i][j-i]:
					m[i][j-i]=q
					s[i][j-i-1]=k

				#print(m)
	print(m)
	print(s) 
#matrix_parentheses2(p)

	