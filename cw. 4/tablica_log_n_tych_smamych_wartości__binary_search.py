#zad. 2 (o) - Dana jest tablica A o długości n. Wartości w tablicy pochodzą ze zbioru B, gdzie ∣B∣ = log n. Proszę zaproponować możliwie jak najszybszy algorytm sortowania tablicy A.

import math

A=[7,2,3,2,7,2,7,7,3,2,3,7,7,3,3,2,3,7]


def binary_search(tab, x):
    l=0
    r=len(tab)-1
    if r==0:
        if tab[0]==x:
            return 0
        else:
            return -1
    while l <= r:
        mid =l + (r - 1)// 2
        if tab[mid] == x:
            return mid
        elif tab[mid] > x:
            r = mid - 1
        else:
            l = mid + 1

    return -1

def sort_log(A):
    values=[]

    for el in A:
        if binary_search(values,el)==-1:
            values=[x for x in values if x < el] + [el] + [x for x in values if x > el]
    print(values)

    C=[0]*len(values)
    B=[0]*len(A)
    
    for el in A:
        idx=binary_search(values,el)
        C[idx]+=1

    for i in range(1,len(C)):
        C[i]=C[i-1]+C[i]

    idx=len(A)-1
    for i in range(len(A)-1,-1,-1):
        j=binary_search(values, A[i])
        C[j]=C[j]-1
        B[C[j]]=A[i]

    print(B)


sort_log(A)



