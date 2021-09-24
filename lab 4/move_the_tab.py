#1.Przesuwanie tablicy w czasie liniowym

A=[1,2,3,4,5,6,7,8,9]

def rev(X,p,k):
	for i in range(p,(k-p)//2+p):
		X[i],X[k-1-i+p]=X[k-i-1+p],X[i]

#jak przekazac tylko cześć mojej tab do funkcji rev?
def move_tab(A,k):
	rev(A,0,len(A))
	rev(A,0,k)
	rev(A,k,len(A))
	#A[0:k]=reversed(A[0:k])
	#A[k:]=reversed(A[k:])
	
move_tab(A,3)
print(A)