class V:
    def __init__(self):
        self.visted=False
        self.parent=None
        self.entry=None
        self.process=None
        self.in_SSS_nr=None


def find_SSS(L):
    time=0
    x=[]
    def DFS_visit(i,T,G):
        nonlocal time,x
        T[i].visted=True
        T[i].entry=time
        time=time+1

        for el in G[i]:
            if T[el].visted==False:
                T[el].parent=i
                DFS_visit(el,T,G)
        T[i].process=time
        time=time+1
        x.append(i)

    T=[0]*len(L)
    for i in range(len(L)):
        T[i]=V()

    for i in range(len(L)):
        if T[i].visted==False:
            DFS_visit(i,T,L)

    for i in range(len(L)):
        T[i].visted=False

    REV=[[] for i in range(len(L))]
    for i in range(len(L)):
        for el in L[i]:
            REV[el].append(i)


    x.reverse()
    which_SSS=0
    for i in range(len(x)):
        if T[x[i]].visted==False:
            which_SSS=which_SSS+1
            T[x[i]].in_SS_nr=which_SSS
            DFS_visit(x[i],T,REV)
        else:
            T[x[i]].in_SS_nr=which_SSS

            
