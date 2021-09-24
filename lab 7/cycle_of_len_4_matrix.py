#cykl dlugosci 4 - rep. macierzowa

G=[[0,1,1,1,0,0,0],
[1,0,1,0,0,0,0],
[1,1,0,0,0,0,0],
[1,0,0,0,1,0,1],
[0,0,0,1,0,1,1],
[0,0,0,0,1,0,1],
[0,0,0,1,1,1,0]]


def Have_cycle(G):
    n=len(G)
    P=[[0]*n for i in range(n)]

    for i in range(n):
        for j in range(n):
            if G[i][j]==1:
                for k in range(j+1,n):
                    if G[i][k]==1:
                        if P[j][k]==1:
                            return True
                        else:
                            P[j][k]=1
    return False

print(Have_cycle(G))