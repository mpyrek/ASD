class Find_Union:
    def __init__(self,val):
        self.val=val
        self.rank=0
        self.parent=self

    def find(self):
        if self!=self.parent:
            self.parent=self.parent.find()
        return self.parent

    def union(self,N):
        N=N.find()
        self=self.find()
        if self==N:
            return
        if N.rank < self.rank:
            N.parent=self
        else:
            self.parent=N
            if self.rank==N.rank:
                N.rank=N.rank+1

G=[[0,1,7],[0,5,1],[1,5,8],[1,2,2],[1,4,3],[2,3,5],[3,4,6],[3,5,4],[4,5,12]]
#graf, n-liczba wierzchołków
def Kruskal(G,n):
    G.sort(key=lambda x:x[2])
    
    T=[0]*n

    for i in range(len(T)):
        T[i]=Find_Union(i)
    A=[]
    for el in G:
        u,v,_ = el
        if T[u].find()!=T[v].find():
            T[u].union(T[v])
            A.append((u,v))
             
    print(A)

Kruskal(G,6)