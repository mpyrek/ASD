from zabtesty import runtests
#zbigniew2 najlepsze (zadanie kolokwium)


#F(i,j)-wykonując i kroków jesteśmy na polu j z energią F(i,j)
def zbigniew1( A ):
    # tu proszę zaimplementować zadanie
    n = len(A)

    F=[[0]*n for i in range(n)] #max ilość skoków może być len(T)
    F[0][0]=A[0]

    for i in range(n):
        for j in range(i,n):
            for k in range(1,F[i][j]+1):
                if j+k==n-1: return i+1
                F[i+1][j+k]=max(F[i][j]-k+A[j+k],F[i+1][j+k])
    return -1

#F(i,j)- będąc na polu i z energią j wykinując F(i,j) kroków [wstępująco]
def zbigniew2( A ):
    # tu proszę zaimplementować zadanie
    n = len(A)
    sum=0
    for i in range(n):
        sum=sum+A[i]

    F=[[1e6]*(sum+1) for i in range(n)]
    F[0][A[0]]=0

    for i in range(n):
        for j in range(sum+1):
            if F[i][j]!=1e6:
                for k in range(1,j+1):
                    if i+k<n:
                        F[i+k][j-k+A[i+k]]=min(F[i][j]+1,F[i+k][j-k+A[i+k]])
    mini=1e6

    for i in range(sum+1):
        mini=min(mini,F[n-1][i])

    if mini!=1e6:
        return mini
    return -1



def zbigniew( A ):
    # tu proszę zaimplementować zadanie
    n = len(A)
    sum=0
    for i in range(n):
        sum=sum+A[i]

    F=[[1e6]*(sum+1) for i in range(n)]
    F[0][A[0]]=0

    for i in range(1,n):
        for j in range(sum+1):
            for k in range(1,i+1):
                if j-A[i]>=0 and j-A[i]+k<sum+1:
                    F[i][j]=min(F[i][j],F[i-k][j-A[i]+k]+1)

    minium=1e6
    for i in range(sum+1):
        minium=min(minium,F[n-1][i])

    if minium!=1e6:
        return minium
    return -1

#print(zbigniew(A))
runtests( zbigniew ) 
