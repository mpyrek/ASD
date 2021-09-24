#Monika Pyrek
# Nasze rozwiązanie  jest analogiczne do LCS.Szukamy LCS od tyłu zapisując wszystkie indeksy(nie tylko pierwszy najdłuższego podciągu) kolejnych elementów w tab. parent.
#  Tym sposobem wypisując nasze rozwiązania, zaczynamy od idx 0. Funkcja find_idx_of_solution pozwala liniowo znależć wszystkie idx, od których zaczynają sie najdłuższe podciągi.
#  Rekurencyjnie wypisujemy i zliczamy poprawne rozwiązania.
# wszystkich możliwych ciągów może być 2^n, więc mimo że funkcja znajdująca ciągi działa w n^2, wypisywanie ich zajmuje więcej czasu. 


C=[2,1,4,3]

def LDS(A):
    n=len(A)
    F=[ 1 for i in range(n)]
    P=[[] for i in range(n)]

    for i in range(n-2,-1,-1):
        for j in range(i+1,n,1):
            if A[j]>A[i]:
                if F[i]<F[j]+1:
                    F[i]=F[j]+1
                    P[i]=[]
                    P[i].append(j)
                elif F[i]==F[j]+1:
                    P[i].append(j)
    #zmienna przetrzymująca dgł. najdłuższych podciągów
    x=max(F)
    #tablica przetrzymująca początkowe indeksy najdłuższych podciągów
    T=find_idx_of_solution(F,x)
    S=[0]*x
    count=0

    def print_solution_rec(A,P,idx,S,i):
        nonlocal count
        if A[idx]:
            S[i]=A[idx]   
            if P[idx]:
                for el in P[idx]:
                    print_solution_rec(A,P,el,S,i+1)
            else: 
                print(S)
                count=count+1

    for el in T:
        print_solution_rec(A,P,el,S,0)

    return count


def find_idx_of_solution(F,x):
    T=[]

    for i in range(len(F)):
        if F[i]==x:
            T.append(i)
    return(T)
    
print(LDS(C))
