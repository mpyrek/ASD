#Zadanie 2. (wybór zadań z terminami) Mamy dany zbiór zadań T = {t1, . . . , tn}. Każde zadanie ti dodatkowo posiada: (a) termin wykonania d(ti) (liczba naturalna) oraz (b) zysk g(ti) za wykonanie w terminie (liczba naturalna). Wykonanie każdego zadania trwa jednostkę czasu. Jeśli zadanie ti zostanie wykonane przed przekroczeniem swojego terminu d(ti), to dostajemy za nie nagrodę g(ti) (pierwsze wybrane zadanie jest wykonywane w chwili 0, drugie wybrane zadanie w chwili 1, trzecie w chwili 2, itd.).
#Proszę podać algorytm, który znajduje podzbiór zadań, które można wykonać w terminie i który prowadzi do maksymalnego zysku. Proszę uzasadnić poprawność algorytmu.

T=[(3,40),(1,30),(4,20),(6,10),(4,70),(2,60),(4,50)]


def greedy_choice(T):
	T.sort(key=lambda x: x[1])
	T=[len(T)]+T
	A=[0]*len(T)

	for i in range(len(T)-1,0,-1):
		idx=T[i][0]
		k=False
		while idx!=0 and k==False:
			if A[idx]==0:
				A[idx]=T[i]
				T.pop()
				k=True
			else:
				idx=idx-1
		if k==False:
			idx=len(A)-1
			while k==False:
				if A[idx]==0:
					A[idx]=T[i]
					T.pop()
					k=True
				else:
					idx=idx-1
	A.pop(0)
	return A

print(greedy_choice(T))