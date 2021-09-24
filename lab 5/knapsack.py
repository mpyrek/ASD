
W=[1,3,2,1,3,2]
P=[3,2,4,5,2,6]

def knapsack(W,P,MaxW):
	n=len(W)
	F=[0]*n
	Par=[0]*n
	for i in range(n):
		F[i]=[0]*(MaxW+1)
		Par[i]=[0]*(MaxW+1)
	for w in range(W[0],MaxW+1):
		F[0][w]=P[0]
	for i in range(1,n):
		for w in range(1,MaxW+1):
			F[i][w]=F[i-1][w]
			Par[i][w]=0
			if w>=W[i]:
				if F[i][w]<(F[i-1][w-W[i]]+P[i]): Par[i][w]=1
				F[i][w]=max(F[i][w],F[i-1][w-W[i]]+P[i])
				
	print(F)
	print(Par)

	i=n-1
	w=MaxW
	while w!=0:
		if Par[i][w]==1:
			#indeks który wzieliśmy, Waga, Profit
			print(i,",",W[i],",",P[i],)
			w=w-W[i]
		i=i-1
	return F[n-1][MaxW]

print(W)
print(P)
print(knapsack(W,P,3)) 