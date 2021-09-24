#Wyobraźmy sobie podziemny labirynt, złożony z ogromnych jaskiń połączonych wąskimi korytarzami. W jednej z jaskiń krasnoludy zbudowały swoją osadę, a w każdej z pozostałych jaskiń mieszka znana krasnoludom ilość trolli. Krasnoludy chcą zaplanować swoją obronę na wypadek ataku ze strony trolli. Zamierzają w tym celu zakraść się i podłożyć ładunek wybuchowy pod jeden z korytarzy, tak aby trolle mieszkające za tym korytarzem nie miały żadnej ścieżki, którą mogłyby dotrzeć do osady krasnoludów.
#Który korytarz należy wysadzić w powietrze, aby odciąć dostęp do krasnoludzkiej osady największej liczbie trolli?

G=[[1,5,6],[0,2,7,8],[3,4],[2],[2],[0,6],[0,5],[1,8],[1,7]]
Z=[3,1,3,1,1,3,3,None,1]

class V:
    def __init__(self):
        self.visted=False
        self.parent=None
        self.entry=None
        self.proces=None
        self.low=None

def find_which_most(G,Z):
    time=0
    
    def DFS_Visit(T,i):
        nonlocal time
        T[i].entry=time
        T[i].low=T[i].entry
        T[i].visted=True
        time=time+1

        for el in G[i]:
            if T[el].visted==True:
                if T[i].parent!=el:
                    T[i].low=T[el].low
            else:
                T[el].parent=i
                DFS_Visit(T,el) 
                T[i].low=min(T[i].low,T[el].low)
        T[i].process=time
        time=time+1
        

    T=[0]*len(G)
    for i in range(len(G)):
        T[i]=V()
        if Z[i]==None:
            parent=i

    DFS_Visit(T,parent)

    for i in range(len(G)):
        T[i].visted=False
    
    def DFS(T,i):
        nonlocal suma
        T[i].visted=True
        suma=suma+Z[i]

        for el in G[i]:
            if T[el].visted==False and el != T[i].parent:
                DFS(T,el)

    suma=0
    max_suma=0
    idx=None

    def DFS_V2(T,par):
        nonlocal idx,suma, max_suma
        T[par].visted=True
        if par!=parent and T[par].entry==T[par].low:
            suma=0
            DFS(T,par)
            if suma>max_suma:
                max_suma=suma
                idx=par
        else:
            for el in G[par]:
                if T[el].visted==False:
                    DFS_V2(T,el)
        
    DFS_V2(T,parent)
    print(T[idx].parent,idx)
    

find_which_most(G,Z)