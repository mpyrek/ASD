#Dana jest tablica A mająca n liczb naturalnych przyjmujących wartości z zakresu [0...n]. Proszę napisać algorytm znajdujący rozmiar największego podzbioru liczb z A, takiego, że ich GCD jest różny od 1. Algorytm powinien działać jak najszybciej.

A=[1,3,6,0,3,7,6,0,3,4,8,10,2,2,12,0,13,4]
import math
0-13

def GCD(x,y):
	while x%y != 0:
		a=x
		x=y
		y=a%y

	return y

def is_prime(x):
	if x==2 or x==3:
	   return True
	for i in range(3,int(math.sqrt(x)),2):
		if x%i==0:
			return False
	return True


def counting_sort(A,n):
	T=[0]*(n+1)
	
	for el in A:
		T[el]=T[el]+1

	max_count=T[0]
	count=T[0]

	for i in range(2,len(T)):
		if is_prime(i):
			for i in range(i,len(T),i):
				count=count+T[i]
			if count>max_count:
				max_count=count
			count=T[0]

	return max_count


print(counting_sort(A,13))