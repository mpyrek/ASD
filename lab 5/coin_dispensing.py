#tablica N[t] dostępnych nominałów, S-kwota do wydania. Obliczyć minimalną liczbę monet do wydania S.
import math
N=[1,5,8]

def spend_money(N,S):
	W=[pow(10,6)]*(S+1) 
	
	for i in range(1,S+1):
		for j in range(len(N)):
			if i==N[j]: W[i]=1
			elif i-N[j]>0 and W[i-N[j]]: W[i]=min(W[i],W[i-N[j]]+1)
	print(W)
	return W[S]

print(spend_money(N,15))