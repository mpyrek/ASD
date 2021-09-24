#mamy dany ciąg napisów S={s1,s2,s3,..sn} oraz pewien napis t. Wiadomo, że napis t można zapisać jako złączenie pewnej ilości napisów S (z powtórzeniami), Na przykład dla S={s1,s2,s3,s4,s5} gdzie s1=ab, s2=abab, s3=ba, s4=bab, s5=b, t=ababbab można zapisać między innymi jako s2s4, s1s1s3s45. Pierwsza reprezentacja ma szerokość 3(przez szerokość rozumiemy długość najkrótszego słow s, użytego w rep. t) a druga1. Proszę opisać algorytm, który mając na wejściu S oraz t znjadzir maks. szerokość rep. t. Proszę oszacowąć czas działania algorytmu.
import math
t="ababbab"
S=["ab","abab","ba","bab","b"]
T=["a","b"]

def the_longest_represenatation(S,t):
	S.sort()
	n=0
	
	l=len(t)-1 #dłg słowa-1
	for el in S: n=max(n,len(el)) #dłg najdłuższego słowa
	F=[0]*(len(t)+1) # F[i]-szerokość naszego słowa jeżeli dochodizmy do i-tej pozycji liczać od końca
	F[len(t)]=pow(10,6)
	for i in range(l,-1,-1):
		for j in range(n):
			if t[i-j:i+1] in S: 
				F[i-j]=max(min(j+1,F[i+1]),F[i-j])
			
	print(F[0:l+1])
	return F[0] #wynik

print(the_longest_represenatation(S,t))