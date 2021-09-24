A=[3,1,7,5,8,6,7,8]

def LIS(T):
    n=len(T)
    F=[1]*len(T)
    P=[-1]*len(T)

    for i in range(1,n):
        for j in range(i):
            if T[i]>T[j] and F[i]<F[j]+1:
                F[i]=F[j]+1
                P[i]=j
    max=0
    idx_max=0
    for i in range(len(F)):
        if max<F[i]:
            max=F[i]
            idx_max=i
    print_solution(T,P,idx_max)

def print_solution(T,P,idx):
    if P[idx]!=-1:
        print_solution(T,P,P[idx])
    print(T[idx])

#LIS(A)

B=[2,10,1,3,1,7,5]
P=[1,3,8,3,3,11,4]


def knap_print_solution(T,Par,i,j):
    if i>=0:
        if Par[i][j]==0:
            knap_print_solution(T,Par,i-1,j)
        elif Par[i][j]==1:
            knap_print_solution(T,Par,i-1,j-T[i])
            print(i, end=' ')

def knapsack(T,P,Max_W):
    F=[[0]*(Max_W+1) for i in range(len(T))]
    Par=[[0]*(Max_W+1) for i in range(len(T))]


    for i in range(T[0],Max_W+1):
        F[0][i]=P[0]
        Par[0][i]=1

    for i in range(1,len(T)):
        for j in range(0,Max_W+1):
            F[i][j]=F[i-1][j]
            if j-T[i]>=0 and F[i][j]<F[i-1][j-T[i]]+P[i]:
                F[i][j]=F[i-1][j-T[i]]+P[i]
                Par[i][j]=1

    knap_print_solution(T,Par,len(T)-1,Max_W)
    print("")
    return F[len(T)-1][Max_W]

#print(knapsack(B,P,3))


def knapsack_2(T,P,Max_W):
    sum_p=0
    for i in range(len(P)):
        sum_p+=P[i]
    
    F=[[-1]*(sum_p+1) for i in range(len(T))]
    
    if T[0]<=Max_W: 
        F[0][P[0]]=T[0]

    for i in range(len(T)):
        if T[i]<=Max_W:
            F[i][P[i]]=T[i]
    

    for i in range(1,len(T)):
        for j in range(sum_p+1):
            if F[i-1][j]!=-1:
                if F[i][j]!=-1:
                    F[i][j]=min(F[i-1][j],F[i][j])
                else:
                    F[i][j]=F[i-1][j]

            if j-P[i]>=0 and F[i-1][j-P[i]]!=-1 and F[i-1][j-P[i]]+T[i]<=Max_W:
                if F[i][j]!=-1:
                    F[i][j]=min(F[i][j],F[i-1][j-P[i]]+T[i])
                else:
                    F[i][j]=F[i-1][j-P[i]]+T[i]
    i=sum_p
    while F[len(T)-1][i]==-1:
        i=i-1
    return i 

#print(knapsack_2(B,P,3))

class Employy:
    def __init__(self,fun):
        self.emp=[]
        self.fun=fun
        self.f=-1
        self.g=-1 


def f(v):
    if v.f>=0:
        return v.f
    x=v.fun
    for emp in v.emp:
        x+=g(emp)
    v.f=max(x,g(v))
    return v.f

def g(v):
    if v.g>=0:
        return v.g
    v.g=0
    for emp in v.emp:
        v.g+=f(emp)
    return v.g



T=[1,3,4,3]

def Sum_Sub(T,x):
    F=[[-1]*(x+1) for i in range(len(T))]

    for i in range(len(T)):
        if T[i]<=x:
            F[i][T[i]]=1
    
    for i in range(1,len(T)):
        for j in range(x+1):
            if F[i-1][j]>=0:
                F[i][j]=1
            if j-T[i]>=0 and F[i-1][j-T[i]]==1:
                F[i][j]=1
    
    if F[len(T)-1][x]==1: return True
    else:
        return False

#print(Sum_Sub(T,2))

k=[1,4,2,3,3]
a=[1,3,8,1,3]


def print_solution_dp(T_1,R,idx_i,idx_j):
    if idx_i>=0 and idx_j>=0:
        if R[idx_i][idx_j]==2:
            print_solution_dp(T_1,R,idx_i-1,idx_j)
        if R[idx_i][idx_j]==1:
            print_solution_dp(T_1,R,idx_i-1,idx_j-1)
            print(T_1[idx_i])
        if R[idx_i][idx_j]==3:
            print_solution_dp(T_1,R,idx_i,idx_j-1)


def LCS(T_1,T_2):
    n=len(T_1)

    F=[[0]*n for i in range(n)]
    R=[[-1]*n for i in range(n)]

    for i in range(n):
        if T_1[0]==T_2[i]:
            F[0][i]=1
            R[0][i]=1

    for i in range(1,n):
        for j in range(n):
            if T_1[i]==T_2[j]:
                if F[i][j]<F[i-1][j-1]+1:
                    F[i][j]=F[i-1][j-1]+1
                    R[i][j]=1
            else:
                if F[i-1][j]>=F[i][j-1]:
                    F[i][j]=F[i-1][j]
                    R[i][j]=2
                else:
                    F[i][j]=F[i][j-1]
                    R[i][j]=3

    idx_j=0
    j=1
    while j<n:
        if F[n-1][idx_j]<F[n-1][j]:
            idx_j=j
        j=j+1
    
    print_solution_dp(T_1,R,n-1,idx_j)
    return F[n-1][idx_j]
    

#print(LCS(k,a))

M=[30,35,15,5,10,20,25]

def print_res(R,i,j):
    if i==j:
        print("(",i,"x",i,")",end=' ')
    else:
        print("(",end=' ')
        print_res(R,i,R[i][j])
        print_res(R,R[i][j]+1,j)
        print(")",end=' ')

def mnoz_macierz(T):
    n=len(T)
    F=[[0]*(n-1) for i in range(n-1)]
    R=[[0]*(n-1) for i in range(n-1)]

    for l in range(2,n):
        for i in range(0,n-l):
            j=i+l-1
            F[i][j]=1e6
            for k in range(i,j):
                if F[i][k]+F[k+1][j]+T[i]*T[k+1]*T[j+1]<F[i][j]:
                    F[i][j]=F[i][k]+F[k+1][j]+T[i]*T[k+1]*T[j+1]
                    R[i][j]=k
    print_res(R,0,n-2)
    return F[0][n-2]

#print(mnoz_macierz(M))


L=[0,1,2,3,4,5]
Pr=[0,1,5,8,9,10]

def pret(Len,Pri,l):
    if l==0:
        return 0
    q=-1e6
    for i in range(l,0,-1):
        q=max(q,Pri[i]+pret(Len,Pri,l-i))

    return q
#print(pret(L,Pr,4))


def mem_pre(Len,Pri,l):
    F=[-1e6]*(l+1)
    F[0]=0
    return mem_pre_a(Len,Pri,l,F)

def mem_pre_a(Len,Pri,l,F):
    if F[l]!=-1e6:
        return F[l]
    q=-1e6
    for i in range(l,0,-1):
        q=max(q,Pri[i]+mem_pre_a(Len,Pri,l-i,F))
    F[l]=q
    return q


#print(mem_pre(L,Pr,4))

def mem_pre_it(Len,Pri,l):
    F=[-1e6]*(l+1)
    F[0]=0

    for i in range(1,l+1):
        q=-1e6
        for j in range(1,i+1):
            q=max(q,Pri[j]+F[i-j])
        F[i]=q

    return F[l]

#print(mem_pre_it(L,Pr,4))


K=[[1,1,1,1],
[1,1,3,4],
[1,1,1,4],
[9,1,2,1]]

def find_path(T):
    for i in range(1,len(T)):
        T[0][i]=T[0][i-1]+T[0][i]
        T[i][0]=T[i-1][0]+T[i][0]

    for i in range(1,len(T)):
        for j in range(1,len(T)):
            T[i][j]=min(T[i-1][j]+T[i][j],T[i][j-1]+T[i][j])

    return T[len(T)-1][len(T)-1]

#print(find_path(K))

MEN=[1,3,2,4,3]

def mentos_problem(T):
    Sum=[[0]*len(T) for i in range(len(T))]
    F=[[0]*len(T) for i in range(len(T))]
    
    for i in range(len(T)):
        Sum[i][i]=T[i]
        F[i][i]=T[i]

    for k in range(1,len(T)):
        for i in range(k,len(T)):
            Sum[i-k][i]=Sum[i-k][i-1]+T[i]

            F[i-k][i]=Sum[i-k][i]-min(F[i-k][i-1],F[i-k+1][i])
    
    return F[0][len(T)-1]
    


#print(mentos_problem(MEN))

F="abfcfckba"

def palindrom(S):
    n=len(S)
    F=[[0]*n for i in range(n)]
    max=1
    idx_of_max=0

    for j in range(n):
        for i in range(n):
            if S[j]==S[n-i-1]:
                if j==0 or i==0:
                    F[j][i]=F[j][i]+1
                else:
                    F[j][i]=F[j-1][i-1]+1
            if F[j][i]>max:
                max=F[j][i]
                idx_of_max=j

    
    return S[idx_of_max-max+1:idx_of_max+1]

#print(palindrom(F))

S="ababbab"
T=["ab","abab","ba","bab","b"]

def slowo(S,T):
    F=[0]*len(S)

    for i in range(len(S)-1,-1,-1):
        for el in T:
            if len(el)+i<=len(S) and el==S[i:i+len(el)]:
                if i+len(el)==len(S):
                    F[i]=max(F[i],len(el))
                else:
                    F[i]=max(F[i],min(len(el),F[i+len(el)]))
    return F[0]

#print(slowo(S,T))

T=[[5,5,5,5,25],
[7,3,1,7,5],
[1,10,1,10,10]]

def pascal(T,k):
    S=[[0]*len(T[0]) for i in range(len(T))]
    F=[[0]*k for i in range(len(S))]
    
    for i in range(len(S)):
        S[i][0]=T[i][0]


    for i in range(len(S)):
        for j in range(1,len(S[i])):
            S[i][j]=S[i][j-1]+T[i][j]

    
    for i in range(k):
        F[0][i]=S[0][i]

    for i in range(1,len(S)):
        for p in range(k):
            F[i][p]=F[i-1][p]
            for x in range(p+1):
                if x>0:
                    F[i][p]=max(F[i][p],F[i-1][x-1]+S[i][p-x])
                else:
                    F[i][p]=max(F[i][p],S[i][p-x])
    return F[len(T)-1][k-1]

#print(pascal(T,4))

