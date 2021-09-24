#Mamy pewien układ klocków domino. Otrzymujemy go w postaci listy par [a, b]: Jeżeli przewrócimy klocek a, to klocek b też się przewróci. Chcemy znaleźć minimalną liczbę klocków, które trzeba przewrócić ręcznie, aby wszystkie domina były przewrócone.

L=[[3],[0],[1],[1,4],[5],[6],[4],[8],[9],[7]]

class V:
    def __init__(self):
        self.visted=False
        self.entry=None
        self.process=None


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

    x.reverse()
    for i in range(len(L)):
        T[i].visted=False

    ile_klocków=0
    for i in range(len(x)):
        if T[x[i]].visted==False:
            ile_klocków=ile_klocków+1
            DFS_visit(x[i],T,L)


    return(ile_klocków)
    



print(find_SSS(L))
    




