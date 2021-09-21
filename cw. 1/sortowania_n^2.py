#sortowanie bąbelkowe 

G=[3,1,2,5,6,3,7,1]

def bubble_sort(T):
    n=len(T)

    for i in range(n):
        for j in range(n-i-1):
            if T[j]>T[j+1]:
                T[j],T[j+1]=T[j+1],T[j]

    return T

#print(bubble_sort(G))            

def better_bubble_sort(T):
    n=len(T)

    for i in range(n):
        swapped=False
        for j in range(n-i-1):
            if T[j]>T[j+1]:
                T[j],T[j+1]=T[j+1],T[j]
                swapped=True
        if swapped==False:
            break
    return T

#print(better_bubble_sort(G))

def insertion_sort(T):
    n=len(T)

    for i in range(1,n,1):
        j=i-1
        key=T[i]
        while j>=0 and T[j]>key:
                T[j+1]=T[j]
                j=j-1
        T[j+1]=key

    return T

#print(insertion_sort(G))


def select_sort(T):
    n=len(T)

    for i in range(n):
        idx_of_min=i
        for j in range(i,n):
          if T[idx_of_min]>T[j]:
              idx_of_min=j
        T[idx_of_min],T[i]=T[i],T[idx_of_min]

    return T
    
print(select_sort(G))

