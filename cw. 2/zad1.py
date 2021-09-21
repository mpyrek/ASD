from random import randint, seed

def mergesort(T):
	#print("Tu proszę napisać swoją funckję")
	if len(T) > 1:
		mid=len(T)//2
		L=T[:mid]
		R=T[mid:]

		mergesort(L)
		mergesort(R)


		i=j=k=0
		while i<len(L) and j<len(R):
			if L[i]<=R[j]:
				T[k]=L[i]
				i=i+1
			else:
				T[k]=R[j]
				j=j+1
			k=k+1
	
		while i<len(L):
			T[k]=L[i]
			i=i+1
			k=k+1
		while j<len(R):
			T[k]=R[j]
			k=k+1
			j=j+1

	return T

seed(42)

n = 10
T = [ randint(1,10) for i in range(10) ]

print("przed sortowaniem: T =", T) 
T = mergesort(T)
print("po sortowaniu    : T =", T)

for i in range(len(T)-1):
  if T[i] > T[i+1]:
    print("Błąd sortowania!")
    exit()
    
print("OK")