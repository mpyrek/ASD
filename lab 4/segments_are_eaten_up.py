#odcinki pozostają nie usuniete jezeli nie zawierają sie w innych

A=[(1,4),(2,8),(4,5),(4,5),(7,9),(8,9)]
B=[(4,5),(7,9),(1,4),(8,9),(2,8)]
C=[(0,3),(0,6),(1,2),(3,4),(5,7),(5,12),(6,7),(8,9),(10,11),(10,13)]


#na poczatku sortujemy tablice B zeby nam powstała tablica A np. heapem

def usuwaj_nie_zawierające(A):
	i=0
	idx=1
	while idx!=len(A):
		if idx!=len(A)-1 and A[idx][1]>A[idx-1][1]: i+=1
		else:
			for i in range(i,idx):
				del(A[i])
			idx=i #lub i=idx
		idx+=1
	return(A)
print(usuwaj_nie_zawierające(C))


G=[(0,3),(0,6),(1,2),(3,4),(5,7),(5,12),(6,7),(8,9),(10,11),(10,13)]

def zawierają_się(B):
	idx_a=idx_a_max=0
	idx_b=idx_b_max=0

	count=max_count=0
	i=0
	idx_a=idx_a_max=B[i][0]
	idx_b=idx_b_max=B[i][1]
	i=i+1
	
	while i<len(B):
		if idx_a==B[i][0]:
			if idx_b<=B[i][1]:
				idx_b=B[i][1]
				count=count+1
			elif idx_b>=B[i][1]:
				count=count+1
			i=i+1
		if idx_a<=B[i][0]:
			if idx_b>=B[i][1]:
				count=count+1
			else:
				if max_count<count:
					max_count=count
					idx_a_max=idx_a
					idx_b_max=idx_b

				idx_a=B[i][0]
				idx_b=B[i][1]
				count=0
			i=i+1
	
	if max_count<count:
		max_count=count
		idx_a_max=idx_a
		idx_b_max=idx_b

	print(idx_a_max,idx_b_max)
	return max_count

#print(zawierają_się(C))