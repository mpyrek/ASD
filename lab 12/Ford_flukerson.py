from collections import deque

G1=[[[2,3],[4,4]],[],[[5,2],[3,2]],[[1,5]],[[5,2]],[[1,4]]]

G2=[[0,0,3,0,4,0],
    [0,0,0,0,0,0],
    [0,0,0,2,0,2],
    [0,5,0,0,0,0],
    [0,0,2,0,0,0],
    [0,4,0,0,0,0]
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
    


def ford_flukeroson(G,s,t):
    max_flow=0

    F=[[None]*len(G) for i in range(len(G))]

    for i in range(len(G)):
        for j in range(len(G[i])):
            F[i][j]=0
            
        
    
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
    print(F)
 
    return max_flow 

    

print(ford_flukeroson(G2,0,1))


