T=[1,2,3,3,3,3,4,5,6,7,9]

def binary_search(T,n,a):
    left=0
    right=n-1
    if right==0 and T[0]==a:
        return 0

    while left<right:
        mid=(left+right)//2

        if T[mid]==a:
            while mid>0 and T[mid-1]==a:
                mid=mid-1
            return mid
        elif T[mid]>a:
            right=mid-1
        else:
            left=mid+1
    return None

print(binary_search(T,len(T),0))
    




