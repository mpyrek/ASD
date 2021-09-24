#Zadanie 3. Dany jest zbiór klocków K = {K1, . . . , Kn}. Każdy klocek Ki opisany jest jako jednostronnie domknięty przedział (ai, bi], gdzie ai, bi ∈ N, i ma wysokość 1 (należy założyć, że żadne dwa klocki nie zaczynają się w tym samym punkcie, czyli wartości ai są parami różne). Klocki są zrzucane na oś liczbową w pewnej kolejności. Gdy tylko spadający klocek dotyka innego klocka (powierzchnią poziomą), to jest do niego trwale doczepiany i przestaje spadać. Kolejność spadania klocków jest poprawna jeśli każdy klocek albo w całości ląduje na osi liczbowej, albo w całości ląduje na innych klockach. Rozważmy przykładowy zbiór klocków K = {K1, K2, K3, K4}, gdzie: K1 = (2, 4], K2 = (5, 7], K3 = (3, 6], K4 = (4, 5].
#Kolejność K1, K4, K2, K3 jest poprawna (choć są też inne poprawne kolejności) podczas gdy kolejność K1, K2, K3, K4 poprawna nie jest (K3 nie leży w całości na innych klockach)



K1 = [2, 4]
K2 = [5, 7]
K3 = [3, 6]
K4 = [4, 5] 
K5 = [6, 7]

K=[K1,K2,K3,K4,K5]
#Patrz zeszyt-znajdziesz lepssze rozwiżaniee :D 
#najpierw sortujemy naszą tablice po zmiennej a malejaco

def block(K):
	K.sort()
	K.reverse()

	for i in range(len(K)):
		K[i].append(0)

	chceck=False
	s=[]
	i=len(K)-1

	while (len(K)-1)>=0 and chceck is not True:
		x=K[i][1]

		if i==len(K)-1:
			s.append(K.pop())
		else:
		   s.append(K[i])
		   K[i][2]==(1)

		check_that_can_put=False
		for j in range(len(K)-1,-1,-1):
			if K[j][0]==x:
				i=j
				K[j][2]=1
				check_that_can_put=True
		if check_that_can_put==False:
			while len(K)!=0 and K[len(K)-1][2]==1:
				K.pop()
			if len(K)>0: i=len(K)-1
			else: chceck==True

	for i in range(len(s)):
		s[i].pop()

	print(s)
		

#block(K)

def klocki(K):
	F=[0]*(len(K)*2)
	j=0
	for i in range(len(K)):
		F[j]=(K[i][0],i,0)
		F[j+1]=(K[i][1],i,1)
		j=j+2
	F.sort(key=lambda x: x[2],reverse=True)
	F.sort(key=lambda x: x[0])
	
	visted=[False]*len(K)
	check=0
	idx_rozpoczęty=None
	idx_końca=None
	flag=True
	k=0

	while flag==True and k<len(F):
		while k<len(F) and visted[F[k][1]]==True:
			k=k+1
		for i in range(k,len(F)):
			if visted[F[i][1]]==False:
				if F[i][2]==0 and idx_rozpoczęty==None:
					idx_rozpoczęty=i
					if check!=0 and F[idx_rozpoczęty][0]!=F[idx_końca][0]:
						flag=False
					idx_końca=None
				elif F[i][2]==0 and idx_rozpoczęty!=None:
					check=check+1
				elif F[i][2]==1 and idx_rozpoczęty==None and F[idx_końca][0]!=F[i][0]:
					flag=False
				elif F[i][2]==1 and idx_rozpoczęty==None and F[idx_końca][0]==F[i][0]:
					check=check-1
				elif F[i][2]==1 and F[idx_rozpoczęty][1]==F[i][1]:
					visted[F[i][1]]=True
					idx_końca=i
					idx_rozpoczęty=None
				elif F[i][2]==1 and (idx_rozpoczęty!=None or F[idx_końca][0]==F[i][0]):
					check=check-1
			

		if check>0:
			flag=False
	print(flag)
    			
klocki(K)	
	
