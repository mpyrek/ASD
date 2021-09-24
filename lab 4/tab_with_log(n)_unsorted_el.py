A=[1,3,5,122,13,19,37,51,67,84,8,101,111,123,14,199]

import math
#n+m+log(n)loglog(n)


def OK_Merge(tab, l, div, r,temp):
	for i in range(l, r + 1):
		temp[i] = tab[i]

	l_i = l
	r_i = div + 1
	c_i = l

	while l_i <= div and r_i <= r:
		if temp[l_i] <= temp[r_i]:
			tab[c_i] = temp[l_i]
			l_i += 1

		else:
			tab[c_i] = temp[r_i]
			r_i += 1

		c_i += 1

	while l_i <= div:
		tab[c_i] = temp[l_i]
		c_i += 1
		l_i += 1



def merge2(tab, l, r,temp):
	div = (l + r) // 2

	if l < r:
		merge2(tab, l, div,temp)
		merge2(tab, div + 1, r,temp)
		OK_Merge(tab, l, div, r,temp)


def merge_sort3(T):
	temp = []
	for i in range(len(T)):
		temp.append(0)

	merge2(T, 0, len(T) - 1,temp)
	return T




def sort_tab_with_log_n(T):
	n=len(T)
	Check=[0]*math.floor(math.log2(n))
	idx=0
	for i in range(n):
		if T[i]%2==0:
			Check[idx]=T[i]
			idx=idx+1
	merge_sort3(Check)

	idx=0
	i=0
	j=0
	Res=[0]*n
	while i!=math.floor(math.log2(n)):
		if T[j]%2==0:
			j=j+1
		else:
			if T[j]<Check[i]:
				Res[idx]=T[j]
				j=j+1
			else:
				Res[idx]=Check[i]
				i=i+1
			idx=idx+1

	while idx!=n:
		if T[j]%2!=0:
			Res[idx]=T[j]
			idx=idx+1
		j=j+1

	return Res

print(sort_tab_with_log_n(A)) 

