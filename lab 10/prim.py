from queue import PriorityQueue

class V:
    def __init__(self,i):
        self.i=i
        self.visted=False
        self.w=float('inf')
        self.childreen=[]

L=[[[1,7],[5,0]],[[0,7],[2,2],[4,3],[5,8]],[[1,2],[3,5]],[[2,5],[4,6],[5,4]],[[3,6],[1,3],[5,12]],[[0,1],[1,8],[3,4],[4,12]]]

def Prim(G):
    T=[0]*len(G)
    
    for i in range(len(G)):
        T[i]=V(i)
    
    Q=PriorityQueue()
    Q.put(0)

    while Q.empty()==False:
        i=Q.get()

        for el in G[i]:
            if T[el[0]].w>el[1]:
                T[el[0]].w=el[1]
                T[el[0]].parent=i
                Q.put(el[0])
                
    
    for i in range(len(T)):
        if T[i].parent is not None:
            T[T[i].parent].childreen.append(i)
    
    

Prim(L)
    
            

    
