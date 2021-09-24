#  była tablica punktów (structy z intami x, y). Punkt 1 dominuje 2 gdy x1 > x2 i y1 > y2 i trzeba było podać liczność najmniejszego zbioru z nich by wybrane punkty dominowały wszystkie niewybrane. Trzeba było w 1-2 zdaniach opisać działanie.

P=[(2,2),(1,1),(2.5,0.5),(3,2),(0.5,3)]

def merge_sort(T,key):
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
			if temp[left_indi][key] >= temp[right_indi][key]:
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

T=[(2,2),(1,1),(2.5,0.5),(3,2),(0.5,3)]


def dominate(T):
	merge_sort(T,1)
	S=[0]*len(T)

	for i in range(len(T)):
		T[i]=(T[i][0],T[i][1],i)
		S[i]=(T[i][0],T[i][1],i)

	merge_sort(S,0)
	
	i=len(S)-1
	start=0
	results=[]

	while i>=0:
		x=S[i]
		if x[2]>=start:
			start=x[2]+1
			results.append((x[0],x[1]))
		i=i-1

	return results
	

	
print(dominate(T))