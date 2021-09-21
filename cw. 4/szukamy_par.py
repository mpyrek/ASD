#Dana jest tablica A oraz liczba k. Znaleźć liczbę różnych par elementów z tablicy A o różnicy równej k.

#Przykład: Dla tablicy [7,11,3,7,3,9,5] oraz k = 4 odpowiedź to 3

T=[7,11,15,7,3,9,5]


def merge_sort(T):
	temp = []
	for _ in range(len(T)):
		temp += [0]

	def Recursion(tab, left_index, right_index):
		div_index = (left_index + right_index) // 2

		if left_index < right_index:
			Recursion(tab, left_index, div_index)
			Recursion(tab, div_index + 1, right_index)
			Merge(tab, left_index, div_index, right_index)


	def Merge(tab, left_index, div_index, right_index):
		for i in range(left_index, right_index + 1):
			temp[i] = tab[i]

		left_indi = left_index
		right_indi = div_index + 1
		curr_indi = left_index

		while left_indi <= div_index and right_indi <= right_index:
			if temp[left_indi] <= temp[right_indi]:
				tab[curr_indi] = temp[left_indi]
				left_indi += 1

			else:
				tab[curr_indi] = temp[right_indi]
				right_indi += 1

			curr_indi += 1

		while left_indi <= div_index:
			tab[curr_indi] = temp[left_indi]
			curr_indi += 1
			left_indi += 1


	Recursion(T, 0, len(T) - 1)

	return T






#liczby są rozróznialen 2 to 2
def find_diffrent_pair(A,k):
	i=0
	j=1
	count=0
	eq=1
	while j<len(A):
		pivot=A[i]
		if pivot+k>A[j]:
			while j<len(A) and pivot+k>A[j]:
				j=j+1

		while j+1<len(A) and A[j]==A[j+1]:
			eq=eq+1
			j+=1

		if j<len(A) and pivot+k==A[j]:
			print(pivot,A[j])
			count=count+eq
			
		i+=1
		eq=1

	return count

def F_P(T):
	merge_sort(T)
	print(T)
	return find_diffrent_pair(T,4)

print(F_P(T))
#liczby są rozróznialne

def find_diffrent_pair2(A,k):
	i=0
	j=1
	count=0
	while j<len(A):
		pivot=A[i]
		if pivot+k>A[j]:
			while j<len(A) and pivot+k>A[j]:
				j=j+1
		if j<len(A) and pivot+k==A[j]:
			print(pivot,A[j])
			count=count+1
			i+=1
			j+=1
		else:
			i+=1

	return count

def F_P2(T):
	merge_sort(T)
	print(T)
	return find_diffrent_pair2(T,4)

print(F_P2(T))





