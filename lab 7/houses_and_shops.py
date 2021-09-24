#Mamy mapę miasteczka, w którym są domy i sklepy. Na mapie są również drogi (każda długości 1), które łączą dom z domem, albo dom ze sklepem. Naszym zadaniem jest, dla każdego domu, znaleźć odległość do najbliższego sklepu.

G=[[1,5],[0,2],[1,3,4],[2,4],[5,3],[0,4]]
T=[[1,5],[0,2],[1,3],[2,6],[6],[0],[3,4]]


from queue import Queue

def find_path(G,S):
    Q=Queue()
    L=[None]*len(G)
    for el in S:
        Q.put(el)
        L[el]=0

    while Q.empty()==False:
        x=Q.get()

        for el in G[x]:
            if L[el]==None or L[el]>L[x]+1:
                L[el]=L[x]+1
                Q.put(el)
            
    for i in range(len(G)):
        print(i,": ",L[i])

#find_path(G,[1,4])
find_path(T, [0,6])
    