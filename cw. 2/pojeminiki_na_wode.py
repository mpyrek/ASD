A=[[[1,4],[2,0]],[[3,5],[7,3]],[[8,4],[10,1]],[[11,8],[14,4]],[[15,2],[20,1]]]


def merge_sort(A):
	if len(A)>1:
		mid=len(A)//2
		L=A[0:mid]
		R=A[mid:]

		merge_sort(L)
		merge_sort(R)

		j=i=k=0
		while i<len(L) and j<len(R):
			if L[i][0][1]<=R[j][0][1]:
				A[k]=L[i]
				i=i+1
			else:
				A[k]=R[j]
				j=j+1
			k=k+1

		while i<len(L):
			A[k]=L[i]
			i=i+1
			k=k+1
		while j<len(R):
			A[k]=R[j]
			j=j+1
			k=k+1
		
		return A


def count_v(x):
	a=x[1][0]-x[0][0]
	b=x[0][1]-x[1][1]
	return a*a*b


def nalewaj_wode(A,V):
	count=0
	i=0
	A=merge_sort(A)
	print(A)
	while i <len(A):
		print(A[i],count)
		nalane_do_pełna=[]
		v_i=count_v(A[i])

		if V<v_i:
		   return count
		else:
			nalane_do_pełna.append(A[i])
			V=V-v_i

		j=i+1
		if j<len(A):

			while A[i][0][1]==A[j][0][1] and j<len(A):
				V=V-count_v(A[j])
				nalane_do_pełna.append(A[j])
				if V<0: return count
				else:
					j=j+1
			
			i=i+len(nalane_do_pełna)-1

			while j<len(A) and A[i][0][1]>A[j][1][1]:
				x=A[i][0][1]-A[j][1][1]
				v_j=x*(A[j][1][0]-A[j][0][0])*(A[j][1][0]-A[j][0][0])
				A[j][1][1]=A[i][0][1]
				V=V-v_j
				if V<0: return count
				j=j+1

	
		i=count+len(nalane_do_pełna)
		count=count+len(nalane_do_pełna)


	return(count)

#print(nalewaj_wode(A,32))

def merge_sort2(A):
	if len(A)>1:
		mid=len(A)//2
		L=A[0:mid]
		R=A[mid:]

		merge_sort2(L)
		merge_sort2(R)

		j=i=k=0
		while i<len(L) and j<len(R):
			if L[i][0]<=R[j][0]:
				A[k]=L[i]
				i=i+1
			else:
				A[k]=R[j]
				j=j+1
			k=k+1

		while i<len(L):
			A[k]=L[i]
			i=i+1
			k=k+1
		while j<len(R):
			A[k]=R[j]
			j=j+1
			k=k+1
		
		return A

def nalewaj_wode2(A,V):
	B=[0]*len(A)*2
	j=0
	for i in range(len(A)):
		width=A[i][1][0]-A[i][0][0]
		B[j]=(A[i][1][1],width,"start")
		B[j+1]=(A[i][0][1],width,"koniec")
		j=j+2

	count=0
	B=merge_sort2(B)

	width=h=h_prev=0
	i=0
	while i<len(B) and V>=0:
		if B[i][2]=="start":
			if h<B[i][0]:
				h=B[i][0]-h_prev
				h_prev=B[i][0]
				V=V-width*h
			width=width+B[i][1]*B[i][1]

		else:
			if h<B[i][0]:
				h=B[i][0]-h_prev
				h_prev=B[i][0]
				V=V-width*h
			width=width-B[i][1]*B[i][1]
			if V>=0:
			   count=count+1

		i=i+1
	
	return count

print(nalewaj_wode2(A,57))




		
