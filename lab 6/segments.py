L=[[0,2],[2,6],[5,8],[0,1],[1,3],[4,6],[6,8],[12,14],[12,13],[10,12],[9,10],[11,12],[10,11],[8,9],[7,10]]

L1=[[0,2,1],[2,6,1],[5,8,1],[0,1,1],[1,3,1],[4,6,1],[6,8,1],[12,14,3],[12,13,2],[10,12,3],[9,10,1],[11,12,5],[10,11,0],[8,9,3],[7,10,1]]

#tablica P przypisuje idx danej współrzędnej (na początku jednak jest to funkcja trzymajaca (współrzędna,początek:koniec,idx w poźniejszym P, idx w wyjściowej tab) 
#mapujemy odcinki tak ze drugi indeks kazdego punku odpowiada indeksowi w tablicy P
#dzięki zmapowaniu wchodząc do odcinka o współrzędnej odblokowanej odblokowujemy współrzedną końca odcinka
def map_odc(L,P,j):
    for i in range(len(L)):
        # 0-początek 1-Koniec
        P[j]=[L[i][0],0,None,i]
        P[j+1]=[L[i][1],1,None,i]
        j=j+2
    P.sort(key=lambda x: x[0])  # O(2*n)
  
    j=0
    P[j][2]=0
    for i in range(1,len(P)):
        if P[i][0]==P[i-1][0]:
            P[i][2]=j
        else:
            j=j+1
            P[i][2]=j
    
    for i in range(len(P)):
        L[P[i][3]][P[i][1]]=(P[i][0],P[i][2])
    L.sort(key=lambda x: x[0][0])
    return j

# O(n)
def can_get_ab(L,a,b):
    P=[False]*len(L)*2
    k=0
    k=map_odc(L,P,k)
    P=[False]*(k+1)
    j=0
    while L[j][0][0]!=a:
        j=j+1
    P[L[j][0][1]]=True
    flag=-1
    while j<k+1 and  L[j][0][0]<=b and flag!=1:
        if P[L[j][0][1]]==True:
            P[L[j][1][1]]=True
            if L[j][1][0]==b:
                flag=1
        j=j+1

    print(flag)

#can_get_ab(L,7,13)

def can_get_the_min_cost_of_ab(F,a,b):
    P=[False]*len(F)*2
    k=0
    k=map_odc(F,P,k)
    P=[1e6]*(k+1)
    j=0
    while F[j][0][0]!=a:
        j=j+1
    P[F[j][0][1]]=0
    flag=-1
    idx=None
    while j<k+1:
        if P[F[j][0][1]]!=1e6:
            P[F[j][1][1]]=min(P[F[j][0][1]]+F[j][2],P[F[j][1][1]])
            if F[j][1][0]==b:
                flag=1
                idx=F[j][1][1]
        j=j+1
    if flag!=-1:
        print(P[idx])
    else:
        print(-1)

#can_get_the_min_cost_of_ab(L1,0,14)

def get_sen_with_k_subseg(L,z):
    P=[False]*len(L)*2
    k=0
    k=map_odc(L,P,k)
    P=[[-1]*(z+1) for i in range(k+1)]
    j=0
    P[0][0]=0
    while j<k+1:
        for i in range(0,z): #dochodzimy do z-1 bo jak mamy juz z kawałków to nie chchemy powikszac
            if P[L[j][0][1]][i]!=-1:
                P[L[j][1][1]][i+1]=max(P[L[j][0][1]][i]+(L[j][1][0]-L[j][0][0]),P[L[j][1][1]][i+1])
        j=j+1
    max_sen=0
    for i in range(k+1):
        max_sen=max(max_sen,P[i][z])
    print(max_sen)
get_sen_with_k_subseg(L,6)