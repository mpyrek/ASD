#Proszę zaproponować algorytm, który na wejście dostaje tablicę A słów (być może o różnych długościach) i sortuje je w porządku słownikowym w czasio O(L), gdzie L to suma długości słów.

A=["aniz","son","babcia","stas","kamil","ati","montek","arek","artur","marek","la","klaudia","blazej","sara","aga","nikodem","helna","t","dominik","hubik","milosz"]

def counting_sort(A,max_len, min_len):
	
	F=[0]*(max_len+1)

	for el in A:
		F[len(el)]=F[len(el)]+1

	for i in range(1,len(F)):
		F[i]=F[i]+F[i-1]

	out=[0]*len(A)

	for i in range(len(A)-1,-1,-1):
		idx=len(A[i])
		F[idx]=F[idx]-1
		out[F[idx]]=(A[i],idx-min_len,idx)
	

	last_min_len=out[0][1]
	A[0]=out[0][0]
	K=[]
	K.append((last_min_len,out[0][2]))
	for i in range(1,len(A)):

		if out[i-1][1]!=out[i][1]:
			last_min_len=i-1
			K.append((last_min_len,out[i][2]))

		A[i]=out[i][0]

	return K




def countin_sort_for_letter(A,start,k):
	F=[0]*26
	
	
	for el in A[start:]:
		F[(ord(el[k-1])-97)]+=1

	for i in range(1,len(F)):
		F[i]=F[i]+F[i-1]

	out=[0]*(len(A)-start)

	for i in range(len(A)-1,start-1,-1):
		idx=ord(A[i][k-1])-97
		F[idx]=F[idx]-1
		out[F[idx]]=A[i]

	A=A[:start]+out
	return A

	

	
def radix_sort1(A,start,k1,k2):
	for i in range(k1,k2,-1):
		A=countin_sort_for_letter(A,start,i)

	return A
		



def radix_sort(A):
	max_len=0
	min_len=1e6
	
	for el in A:
		max_len=max(max_len,len(el))
		min_len=min(min_len,len(el))

	#posortowanie po długości el
	K=counting_sort(A,max_len,min_len)
	i=len(K)-1

	while i!=0:
		radix_sort1(A,K[i][0]+1,K[i][1],K[i-1][1])
		i=i-1

	A=radix_sort1(A,0,K[0][1],0)
	return(A)

print(radix_sort(A))