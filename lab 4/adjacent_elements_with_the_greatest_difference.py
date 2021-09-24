#6 - Dana jest tablica A zawierająca n parami różnych liczb. Proszę zaproponować algorytm, który znajduje takie dwie liczby x i y z A, że y−x jest jak największa oraz w tablicy nie ma żadnej liczby z takiej, że x < y < z (innymi słowy, po posortowaniu tablicy A rosnąco wynikiem byłyby liczby A[i] oraz A[i+1] dla których A[i + 1] − A[i] jest największe).


A=[0,3,14,13,4,9,1,8,12,7,1,2,5,3,8,4,11,15]

def find_the_lowest(A):
	n=len(A)
	norm=(max(A)-min(A)+1)
	F=[[] for i in range(n)]

	for el in A:
		idx=el/norm
		idx=int(idx*n)
		if not F[idx]:
			F[idx]=[el]*2
		else:
			if F[idx][0]>el:
				F[idx][0]=el
			elif F[idx][1] < el:
				F[idx][1]=el
	
	count=0
	max_count=0
	min_el=1e6
	max_el=0
	i=0
	j=1

	print(F)

	while j<n:
		while i<n+1 and not F[i]:
			i+=1
		j=i+1
		if i<n and F[i]:
			max_el=F[i][1]
		while j<n and not F[j]:
			j=j+1
		if j<n and F[j]:
			min_el=F[j][0]

		
		count=min_el-max_el
		if count>max_count:
			max_count=count
		i=i+1
		j=j+1

	print(max_count)

find_the_lowest(A)
