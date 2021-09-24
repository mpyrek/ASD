from collections import deque


G2=[[0,0,0,0,0,10,0,0,0,0,0,0],
    [0,0,0,0,0,12,5,0,0,0,0,0],
    [0,0,0,0,0,0,8,14,0,0,0,0],
    [0,0,0,0,0,0,0,7,11,0,0,0],
    [0,0,0,0,0,0,0,0,2,0,0,0],
    [0,0,0,0,0,0,0,0,0,3,0,0],
    [0,0,0,0,0,0,0,0,0,15,6,0],
    [0,0,0,0,0,0,0,0,0,0,20,13],
    [0,0,0,0,0,0,0,0,0,0,0,18],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0]
    ]



def exist_path(G,s,t):
    if s==t:
        return True

    for i in range(len(G[s])):
        if G[s][i]!=0:
            return exist_path(G,i,t)

    return False

def BFS(G,s,t):
    visted=[False for i in range(len(G))]
    parent=[None for i in range(len(G))]
    flow=[float('inf') for i in  range(len(G))]


    Q=deque()
    Q.append(s)

    while Q:
        x=Q.pop()
        visted[x]=True
        if x==t:
            return (flow[t],parent)
        
        for i in range(len(G[x])):
            if G[x][i] != 0:
                parent[i]=x
                flow[i]=min(G[x][i],flow[x])
                Q.append(i)
    


def ford_flukeroson(G,S,T):
    max_flow=0
    G.append([])
    G.append([])

    for i in range(len(G)):
        if i<len(G)-2:
            G[i].append(0)
            G[i].append(0)
        G[len(G)-1].append(0)
        G[len(G)-2].append(0)


    for el in S:
        G[len(G)-2][el]=float('inf')

    for el in T:
        G[el][len(G)-1]=float('inf')

    F=[[0]*len(G) for i in range(len(G))]

    s=len(G)-2
    t=len(G)-1
    
    while exist_path(G,s,t):
        flow,P=BFS(G,s,t)
        max_flow+=flow
        idx=t
        while P[idx]!=None:
            #krawędź istnieje w G
            if G[P[idx]][idx]!=0:
                F[P[idx]][idx]+=flow
                G[P[idx]][idx]-=flow
            else:
                F[P[idx]][idx]-=flow
                G[P[idx]][idx]+=flow
            idx=P[idx]
 
    return max_flow 

S=[0,1,2,3,4]
T=[9,10,11]

print(ford_flukeroson(G2,S,T))


