#Bajtocja jest krainą zawierającą N miast, N-1 dwukierunkowych dróg i układ dróg tworzy graf spójny. Mając listę K miast do których musimy dostarczyć przesyłki i mogąc wystartować i zakończyć trasę w dowolnym mieście, podaj minimalny dystans, który musimy przebyć, że zrealizować to zadanie.

G=[[1],[0,2,3,9],[1,4],[1],[2],[9],[7,10],[6,8,9],[7,11],[1,5,7],[6],[8]]
K=[1,3,4,5,8,6,9,10]

class V:
    def __init__(self):
        self.visted=False
        self.parent=None
        self.have_list=False



def count_path(G,K):
    T=[0]*len(G)
    for i in range(len(G)):
        T[i]=V()

    for el in K:
        T[el].have_list=True

    def DFS(T,i):
        T[i].visted=True
        for el in G[i]:
            if T[el].visted==False:
                T[el].parent=i
                DFS(T,el)
        if T[i].parent!=None and T[T[i].parent].have_list==False:
            T[T[i].parent].have_list=T[i].have_list


    DFS(T,K[0])# sprawdzamy czy do danego dziecka chcemy wejść 


    def DFS_visit(i,T,L):
        nonlocal len_of_path,idx_of_max
        T[i].visted=True
        for el in G[i]:
            if T[el].visted==False and T[el].have_list==True:
                L[el]=L[i]+1
                T[el].parent=i
                DFS_visit(el, T, L)

                if len_of_path<L[el]:
                    len_of_path=L[el]
                    idx_of_max=el
        
        return idx_of_max
    
    len_of_path=0
    idx_of_max=0
    L=[0]*len(G)
    for i in range(len(G)):
        T[i].visted=False

    v=DFS_visit(K[0],T,L)

    len_of_path=0
    idx_of_max=0
    L=[0]*len(G)
    for i in range(len(G)):
        T[i].visted=False

    z=DFS_visit(v,T,L)

    k=[]
    x=z
    while x!=v:
        k.append(x)
        x=T[x].parent
    k.append(x)

    for i in range(len(G)):
        T[i].visted=False

    len_of_path=len(k)-1

    def DFS(i,T):
        nonlocal len_of_path
        T[i].visted=True

        for el in G[i]:
            if T[el].visted==False and T[el].have_list==True:
                len_of_path=len_of_path+2
                DFS(el,T)

    for el in k:
        T[el].visted=True

    for i in range(len(k)-1):
        for v in G[k[i]]:
            if T[v].have_list==True and T[v].visted==False:
                len_of_path=len_of_path+2
                DFS(v,T)

    print(len_of_path)

count_path(G,K)


def count_path2(G,K):
    T=[0]*len(G)
    for i in range(len(G)):
        T[i]=V()

    for el in K:
        T[el].have_list=True

    def DFS1(T,i):
        T[i].visted=True
        for el in G[i]:
            if T[el].visted==False:
                T[el].parent=i
                DFS1(T,el)
        if T[i].parent!=None and T[T[i].parent].have_list==False:
            T[T[i].parent].have_list=T[i].have_list


    DFS1(T,K[0])# sprawdzamy czy do danego dziecka chcemy wejść 


    def DFS_visit(i,T,L):
        nonlocal len_of_path,idx_of_max
        T[i].visted=True
        for el in G[i]:
            if T[el].visted==False and T[el].have_list==True:
                L[el]=L[i]+1
                T[el].parent=i
                DFS_visit(el, T, L)

                if len_of_path<L[el]:
                    len_of_path=L[el]
                    idx_of_max=el
        
        return idx_of_max
    
    len_of_path=0
    idx_of_max=0
    L=[0]*len(G)
    for i in range(len(G)):
        T[i].visted=False

    v=DFS_visit(K[0],T,L)

    len_of_path=0
    idx_of_max=0
    L=[0]*len(G)
    for i in range(len(G)):
        T[i].visted=False
    v=DFS_visit(v,T,L)

    for i in range(len(G)):
        T[i].visted=False

    len_of_path2=0

    def DFS(T,i):
        nonlocal len_of_path2
        T[i].visted=True
        len_of_path2=len_of_path2+1
        for el in G[i]:
            if T[el].visted==False and T[el].have_list==True:
                DFS(T,el)
        len_of_path2=len_of_path2+1

    DFS(T,v)

    print(len_of_path2-len_of_path-2)

count_path2(G,K)