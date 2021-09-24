#D.P. rozwiązanie zstępujące 
# O(n*sum(P)), pamięć: O(N*sum(P))

W=[3,5,6,3,3]
P=[5,1,7,3,4]

def Knapsack(W,P,MaxW):
    sum=0
    for i in range(len(P)):
        sum=sum+P[i]
    
    T=[[1e6]*(sum+1) for i in range(len(P))]

    #warunek początkowy ustawiamy przy proficie 1 el wage(za kazdym przejscie spr. czy wage nie jest wieksza)
    if W[0]<MaxW:
        T[0][P[0]]=W[0]

    for i in range(1,len(P)):
        for j in range(sum+1):
            if j==P[i] and W[i]<=MaxW:
                T[i][j]=min(T[i-1][j],W[i])
            elif T[i-1][j]!=1e6 and T[i-1][j]+W[i]<=MaxW:
                T[i][j]=T[i-1][j]
                T[i][j+P[i]]=min(T[i][j+P[i]], T[i-1][j]+W[i])


    i=sum
    while i>=0 and T[len(P)-1][i]==1e6:
        i=i-1

    if i==0: return -1
    #(waga,profit)
    return(T[len(P)-1][i],i)

print(Knapsack(W,P,11))