#Zadanie 3. (ładowanie promu) Dana jest tablica A[n] z długościami samochodów, które stoją w kolejce, żeby wjechać na prom. Prom ma dwa pasy (lewy i prawy), oba długości L. Proszę napisać program, który wyznacza, które samochody powinny pojechać na który pas, żeby na promie zmieściło się jak najwięcej aut. Auta muszą wjeżdżac w takiej kolejności, w jakiej są podane w tablicy A.

#rozwiązanie trudne xd
def prom(A,L):
    F=[[-1]*(L+1) for i in range(L+1)]
    #el 1,2,3,4
    A=[0]+A
    P=[[0]*(L+1) for i in range(L+1)]
    
 
    sum=0
    max_val=-1
    idx_of_max_val=0
    for i in range(1,len(A)):
        sum+=A[i]
        if sum<=L:
            F[0][i]=(0,sum)
            P[0][i]=(0,i-1)
            max_val=sum
            idx_of_max_val=(0,i)

    for i in range(1,len(A)):
        for j in range(i+1,len(A)):
            if F[i-1][j-1]!=-1 and F[i-1][j-1][0]+A[j]<=L:
                F[i][j]=(F[i-1][j-1][1],F[i-1][j-1][0]+A[j])
                P[i][j]=(i-1,j-1)
                if max_val<F[i][j][0]+F[i][j][1]:
                    max_val=F[i][j][0]+F[i][j][1]
                    idx_of_max_val=(i,j)

            elif F[i][j-1]!=-1 and F[i][j-1][1]+A[j]<=L:
                F[i][j]=(F[i][j-1][0],F[i][j-1][1]+A[j])
                P[i][j]=(i,j-1)
                if max_val<F[i][j][0]+F[i][j][1]:
                    max_val=F[i][j][0]+F[i][j][1]
                    idx_of_max_val=(i,j)
    T1=[]
    T2=[]
    print_solution(A,F,P,idx_of_max_val[0],idx_of_max_val[1],T1,T2)
    print(T1,T2)

def print_solution(A,F,P,x,y,T1,T2):
    if P[x][y]==0:
        return
    if x-P[x][y][0]==1 and y-P[x][y][1]==1:
        T2.append(y-1)
        print_solution(A,F,P,P[x][y][0],P[x][y][1],T2,T1)
    else:
        T2.append(y-1)
        print_solution(A,F,P,P[x][y][0],P[x][y][1],T1,T2)



def port2(A,L):
    F=[]
    for k in range(len(A)):
        F.append([])
        for i in range(L+1):
            F[k].append([])
            for j in range(L+1):
                F[k][i].appenrd(0)
    
    F[0][L][L]=0
        


#rozw. łatwe
#F[i,l1,l2]=F[i-1,l1-W[i],l2],F[i-1,l1,l2-W[i]




B=[5,5]
prom(B,5)