#Floyd-Warhsall
#najkrotsze_sciezki_miedzy_kazda_para_wierzcholkow_wagi_ujemne

Z=[[[1,2],[2,5]],[[2,2],[4,-5],[3,1]],[[4,7]],[[5,2]],[[3,-2]],[[4,1]]]
F=[[[1,1],[2,5]],[[2,-3]],[[3,1]],[[1,-2]]]

def print_path(P,s,v):
    tab=[]
    while s!=v:
       tab.append(v)
       v=P[s][v]
    tab.append(s)
    tab.reverse()
    print(tab)

def find_all(G):
    S=[[float('inf')]*len(G) for i in range(len(G))]
    P=[[None]*len(G) for i in range(len(G))]

    for i in range(len(G)):
        P[i][i]=i
        for el in G[i]:
            S[i][el[0]]=el[1]
            P[i][el[0]]=i

    for t in range(len(G)):
        for i in range(len(G)):
            for j in range(len(G)):
                if S[i][j] > S[i][t]+S[t][j]:
                    S[i][j]=S[i][t]+S[t][j]
                    P[i][j]=P[t][j]
                


    #print(P)
    #print(S)
    s=0
    t=5
    print_path(P,s,t)

find_all(Z)
