
A=[-3,9,11,-2,7,-30]

def ssp2(tab,l,r):
	if l>r: return 0
	if l==r: return max(0,tab[l])

	mid=(l+r)//2
	wl=ssp2(tab,l,mid)
	wr=ssp2(tab,mid+1,r)

	sl=sr=0
	par=0
	print(wl)
	print(wr)
	for i in range(mid,l-1,-1):
		par=par+tab[i]
		if par>sl: sl=par

	par=0
	for i in range(mid+1,r+1):
		par=par+tab[i]
		if par>sr: sr=par

	return max(wl,wr,sl+sr)


print(ssp2(A,0,len(A)-1))

def ssp(T):
	par=0
	res=0
	for i in range(len(A)):
		par=par+T[i]
		if par<0: par=0
		if par>res: res=par	
	return res

print(ssp(A))