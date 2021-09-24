#Dana jest tablica A zawierająca n elementów, z których każdy ma jeden z k kolorów. Proszę podać możliwie jak najszybszy algorytm, który znajduje indeksy i oraz j takie, że wsród elementów A[i], A[i + 1], . . . , A[j] występują wszystkie k kolorów oraz wartość j−i jest minimalna (innymi słowy, szukamy najkrótszego przedziału z wszystkimi kolorami).

K=5
A=[1,0,2,2,4,2,4,3,2,2,1,0,0,0,2,2,1]



def unique(A,k):
	count=0
	min_len=1e6
	min_start=0
	min_end=0
	K=[0]*k

	start=0
	end=0

	while end!=len(A):
		if count!=k:
			if K[A[end]]==0: count +=1
			K[A[end]]+=1
			if count!=k: end+=1


		elif count==k:
			if min_len>end-start:
				min_len=end-start
				min_start=start
				min_end=end

			if(start != end):
				print(start,end,K)
				if K[A[start]]>1:
					K[A[start]]-=1
					start+=1

					if min_len>end-start:
						min_len=end-start
						min_start=start
						min_end=end

				else:
					end+=1
					if end<len(A):
					   K[A[end]]+=1

	return min_start,min_end

print(unique(A,5))
		


			
