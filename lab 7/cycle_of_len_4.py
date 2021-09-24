# Proszę podać jak najszybszy algorytm, który znajduje w grafie cykl długości dokładnie 4 (trywialny algorytm ma złożoność O(n^4), gdzie n to liczba wierzchołków---chodzi o rozwiązanie szybsze).

#lista sąsiedztwa
class v:
    def __init__(self,i):
        self.i=i;
        self.visted=False
        self.parent=None
        self.entry=None
        self.process=None

G1=[[1,2],[0,2,3],[0,1,4],[1,4],[2,3]]
G=[[1],[2,3],[0,1],[4],[2]]

def DFS(G):
    time=0

    def DVS_visit(u):
        nonlocal time
        u.entry=time
        u.visted=True
        time=time+1
        
        for v in G[u.i]:
            if T[v].visted==False:
                T[v].parent=u.i
                DVS_visit(T[v])
        u.process=time
        time=time+1

    T=[0]*len(G)
    for i in range(len(G)):
        T[i]=v(i)
    
    for i in range(len(G)):
        if T[i].visted==False:
            DVS_visit(T[i])

    for i in range(len(G)):
        print(T[i].i, T[i].parent,T[i].entry,T[i].process)


DFS(G)