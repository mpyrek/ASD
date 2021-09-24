
class V:
    def __init__(self):
        self.d=float('inf')
        self.parent=None

#graf
L=[[0,1,3],[4,1,2],[1,2,3],[2,3,2],[3,4,-15],[3,5,2]]

def bellman_ford(G,v,s,t):
    T=[0]*v
    for i in range(v):
        T[i]=V()

    
    T[s].d=0

    for i in range(v-1):
        for el in L:
            if T[el[1]].d>T[el[0]].d+el[2]:
                T[el[1]].d = T[el[0]].d+el[2]
                T[el[1]].parent=el[2]

    flag=False
    for el in L:
        if T[el[1]].d>T[el[0]].d+el[2]:
            flag=True
    if flag==False:
        print(T[t].d)
    else:
        print("inf")

bellman_ford(L,6,0,5)