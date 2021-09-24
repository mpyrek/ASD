#program zlicza ilość inwersji w algorytmie merge_sort

T=[1,2,1,4,3,1]

def merge(T,start,mid,end):
    count=0
    i=start
    j=mid+1
    k=start
    W=[]

    while i<mid+1 and j<end+1:
        if T[i] <= T[j]:
            W.append(T[i])
            i=i+1
        else:
            W.append(T[j])
            count=count+mid+1-i
            j=j+1
    
    while i<mid+1:
        W.append(T[i])
        i=i+1
        
    while j<end+1:
        W.append(T[j])
        j=j+1

    i=0

    while start+i<=end:
        T[start+i]=W[i]
        i=i+1

    return count 
    




def merge_sort(T,start,end):
    count=0
    if start!=end:
        mid=(start+end)//2
        count=count+merge_sort(T,start,mid)
        count=count+merge_sort(T,mid+1,end)
        count=count+merge(T,start,mid,end)
    return count

print(merge_sort(T,0,len(T)-1))
