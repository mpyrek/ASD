#ciągły problem plecakowy
#Dana jest n elementowa tablica A = [(P1, W1), . . . ,(Pn, Wn)] opisująca egzemplarz ciągłego problemu plecakowego; A opisuje dostępne płyny a k objętość plecaka (a raczej pojemnika; k jest podane w litrach). Dla i-go przedmiotu Pioznacza jego wartość za wszystkie dostępne Wi litrów. Proszę zaimplementować funkcję knapsack(A,k), która oblicza wartość najlepszego pojemnika, jaki można uzyskać.
#Państwa kod powinien mieć następującą postać (będzie uruchamiany; proszę nie suwać fragmentu testującego; sprawdzający może także dołożyć swoje testy):

def knapsack(A, k):
	T=[0]*len(A)
	for i in range(len(A)):
		T[i]=[A[i],A[i][0]/A[i][1]]
	T.sort(key=lambda x: x[1])
	T.reverse()
	count=0
	i=0
	
	while k!=0 and i<len(T):
		if k-T[i][0][1]>=0:
			k=k-T[i][0][1]
			count=count+T[i][0][0]
			i=i+1
		else:
			count=count+T[i][1]*k
			k=0
			i=i+1
	return count
	
# elementarny test, powinien wypisać 12
print(knapsack([(1,1),(10,2),(6,3)],3))