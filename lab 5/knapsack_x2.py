#max_weight=Max_W
#max_heigth=Max_H

#W[i]-waga naszego przedmiotu
#H[i]-wysokość naszego przedmiotu
#P[i]-wartość naszego przedmiotu

def knapsack_x2(W,H,P,M,S):
	F=[]
	for x in range(0,len(W)):
		F.append([])
		for y in range(0,M+1):
			F[x].append([])
			for z in range(0,S+1):
				F[x][y].append(0)

	
	for i in range(W[0],Max_W+1):
		F[0][i][0]=P[0]
	for i in range(H[0],S+1):
		F[0][0][i]=P[0]
	for i in range(len(W)):
		F[i][0][0]=0

	for i in range(len(W)):
		for w in range(Max_W+1):
			for h in range(Max_H+1):
				F[i][w][h]=F[i-1][w][h]	#tzn. że nie bierzemy tego el

				if w-W[i]>=0:
					if h-H[i]>=0:
						F[i][w][h]=max(F[i][w][h],F[i-1][w-W[i]][h-H[i]]+P[i])	#bierzrmy ten el

	return F[len(W)-1][Max_W][Max_H]

W=[1,2,3,4]
knapsack_x2(W,3,3,3,3)