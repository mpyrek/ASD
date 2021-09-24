#Dany jest zbiór przedziałów otwartych. Zaproponuj algorytm, który znajdzie podzbiór tego zbioru, taki że:
#jego rozmiar wynosi dokładnie k
#przedziały są rozłączne
#różnica między najwcześniejszym początkiem, a najdalszym końcem jest minimalna.
#Jeśli rozwiązanie nie istnieje, to algorytm powinien to stwierdzić. Algorytm powinien być w miarę możliwości szybki, ale przede wszystkim poprawny.

T=[[1,6],[1,4],[2,4],[3,5],[4,6],[5,6],[6,8],[6,7]]

def find_solution(L,k):
    L.sort(key=lambda x: x[1])
    min_len=1e6
    parent=[[] for i in range(len(L))]
    result=[[] for i in range(k)]

    for i in range(len(L)-k):
        l=0
        start=L[i][0]
        idx=i
        j=idx+1
        while j<len(L) and l!=k:
            if L[j][0]>=L[idx][1]:
                parent[j]=idx
                l=l+1
                idx=j
            j=j+1
            
        end=L[idx][1]
        if l==k and end-start<min_len:
            min_len=end-start
            for z in range(k):
                result[z]=L[idx]
                idx=parent[idx]

    if result[0]:
      print(result)
    else:
        print(False)
    
find_solution(T,4)
