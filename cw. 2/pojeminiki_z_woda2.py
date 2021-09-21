A=[[[1,4],[2,0]],[[3,5],[7,3]],[[8,4],[10,1]],[[11,8],[14,4]],[[15,2],[20,1]]]



def mergesort(A):
	if len(A) > 1:
		mid=len(A)//2
		L=A[:mid]
		R=A[mid:]

		mergesort(L)
		mergesort(R)


		i=j=k=0
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
			k=k+1
			j=j+1

		return A


def pojemniki(T,A):
    G=[]

    for i in range(len(T)):
        width=T[i][1][0] -T[i][0][0]
        G.append((T[i][1][1],width,0))
        G.append((T[i][0][1],width,1))

    mergesort(G)
    last=0
    weidth=0
    pojemniki=0
    i=0
    while i <len(G) and A>=0:
        if G[i][2]==0:
            A=A-weidth*(G[i][0]-last)
            last=G[i][0]
            weidth=weidth+G[i][1]
        else:
            A=A-weidth*(G[i][0]-last)
            last=G[i][0]
            weidth=weidth-G[i][1]
            if A>=0:
                pojemniki=pojemniki+1
        i=i+1

    print(pojemniki)





pojemniki(A,35)
    
