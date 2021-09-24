#F[n]=F[n-1]+F[n-2]

def count_string(n):
    F=[0 for i in range(n+1)]
    F[0]=0
    F[1]=2
    F[2]=3

    for i in range(3,n+1):
        F[i]=F[i-1]+F[i-2]
    return F[n]

print(count_string(4))
