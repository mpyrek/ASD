from random import randint, shuffle, seed
from math import ceil
 
 
def insertionSort(arr, start, end, offset):
    for i in range(start+offset, end+1, offset):
        key = arr[i]
        j = i - offset
 
        while j >= start and key < arr[j]:
            arr[j + offset] = arr[j]
            j = j - offset
        arr[j + offset] = key
 
 
def partition(A, start, end, q):
    pivot = q
 
    i = start-1
    j = start
    while j <= end:
        if A[j] < pivot:
            i = i+1
            A[i], A[j] = A[j], A[i]
        elif j < end and A[j] == pivot:
            A[end], A[j] = A[j], A[end]
            j -= 1
        j += 1
    A[i+1], A[end] = A[end], A[i+1]
    return i+1
 
 
#funkcja select zawsze szuka odpowiedniego pivota za pomocą funkcji find_median; 

def Select(A, start, end, k):
    if start == end:
        return A[start]
    x = find_median(A, start, end, 1)
    q = partition(A, start, end, x)
    if q == k:
        return A[q]
    if k < q:
        return Select(A, start, q-1, k)
    else:
        return Select(A, q+1, end, k)
 
#find median szuka meidany do skutku dzialąc el. na piątki. Np. na początku piątki są w jendej częsci tab-offset=1 a następnie wśród tych median szukamy mediany- offset=5 itd.; 
 
def find_median(A, start, end, offset):
    nBlocks = ceil((end-start)/(offset*5))
 
    idx = start
    #funkcje insertion Sort wykonuję nblocks-1 razy, gdzyć ostatnie przejście w tab. może mieć mniejszą ilość el. 
    for i in range(0, nBlocks-1):
        insertionSort(A, idx, idx + 5 * offset - 1, offset)
        idx += offset * 5
    insertionSort(A, start + (nBlocks - 1) * 5 * offset, end, offset)
 
    if nBlocks == 1:
        nMedians = ceil((end-start)/(offset))
        return A[start + (nMedians//2) * offset]
    return find_median(A, start + offset * 2, end, offset*5)
 
 
def linearselect(A, k):
    return Select(A, 0, len(A)-1, k)
 
 
seed(42)
 
n = 100
for i in range(n):
    A = list(range(n))
    shuffle(A)
    # print(A)6
    x = linearselect(A, i)
    if x != i:
        print("Blad podczas wyszukiwania liczby", i)
        exit(0)
 
print("OK")