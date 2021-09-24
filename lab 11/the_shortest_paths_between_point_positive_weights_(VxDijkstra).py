#|V|  razy algorytm dijkstry - O(VElogV)
from queue import PriorityQueue

G=[[(1,2),(2,5)],[(2,2),(4,5),(3,1)],[(4,7)],[(5,2)],[],[(4,1)]]

class V:
    def __init__(self):
        self.d=float('inf')
        self.parent=None
        self.visted=False

def print_solution(T,s,t):
    if s!=t and T[t].parent!=None:
        print_solution(T,s,T[t].parent)
    print(t)
    

def find_path(G):
    T=[0]*len(G)

    for i in range(len(G)):
        T[i]=V()

    for i in range(len(G)):
        for j in range(len(G)):
            T[j].d=float('inf')
            T[j].parent=None
            T[j].visted=False
        T[i].d=0
        Q=PriorityQueue()
        Q.put((0,i))

        while Q.empty()==False:
            dist , x= Q.get()
            T[x].visted=True

            for v in G[x]:
                if T[v[0]].visted==False and v[1]+dist < T[v[0]].d:
                    T[v[0]].d= dist +v[1]
                    T[v[0]].parent=x
                    Q.put((T[v[0]].d,v[0]))

        
        for j in range(len(G)):
            if i!=j  and T[j].d != float('inf'):
                print("ścieżka z ", i, "do ",j,": ")
                print_solution(T,i,j)
                    
find_path(G)
        
        
    