#Problem wybierania zajęć

class Zajęcia:
	def __init__(self,pocztek,koniec):
		self.początek=pocztek
		self.koniec=koniec

A=Zajęcia(2,3)

n=12
A=[0]*n

A[0]=Zajęcia(0,0)
A[1]=Zajęcia(1,4)
A[2]=Zajęcia(3,5)
A[3]=Zajęcia(0,6)
A[4]=Zajęcia(5,7)
A[5]=Zajęcia(3,9)
A[6]=Zajęcia(5,9)
A[7]=Zajęcia(6,10)
A[8]=Zajęcia(8,11)
A[9]=Zajęcia(8,12)
A[10]=Zajęcia(2,14)
A[11]=Zajęcia(12,16)

#s-początek zajęc, f-koniec zajęc, k-nr odcinka(zajęć), n-koniec naszego przedizału [żeby wszystko było ok na pocżątek doodajemy odcinek ończący sie na 0] (s,f,0,n)
P=[0]*n
def recursive_activity_selector(A,k,n):
	m=k+1
	while m<n and A[m].początek<A[k].koniec:
		m=m+1
	if m<n:
		P[m]=1
		return recursive_activity_selector(A,m,n)
	else: return False

#recursive_activity_selector(A,0,n)
#print(P)

for i in range(n):
	if P[i]==1:
		print(i,A[i].początek,A[i].koniec)

#iteracyjnie
G=[]
def greedy_activity_selector(A):
	n #mamy dane
	G.append(A[1].początek)
	G.append(A[1].koniec)
	G.append("|")
	k=1
	for m in range(2,n):
		if A[k].koniec<=A[m].początek:
			G.append(A[m].początek)
			G.append(A[m].koniec)
			G.append("|")
			k=m
	print(G)
	return G
#greedy_activity_selector(A)


#poprzez algorytm dynamiczny

B=[(1,4),(3,5),(0,6),(5,7),(3,9),(5,9),(6,10),(8,11),(8,12),(2,14),(12,16)]

def dynamic_activity_selector(X,n):
	L=[[] for i in range(n)]

	for i in range(n):
		for j in range(i):
			start,finish=(X[i][0],X[j][1])
			if finish<=start and len(L[j])>len(L[i]):
				L[i]=L[j].copy()
		L[i].append(X[i])		
	print(L)
	return(L[n-1])
print(dynamic_activity_selector(B,len(B)))