#(wędrówka po szachownicy) Dana jest szachownica A o wymiarach n × n. Szachownica zawiera liczby wymierne. Należy przejść z pola (1, 1) na pole (n, n) korzystając jedynie z ruchów “w dół” oraz “w prawo”. Wejście na dane pole kosztuje tyle, co znajdująca się tam liczba. Proszę podać algorytm znajdujący trasę o minimalnym koszcie.
K=[[0,1,2,3],[0,-2,3,2,],[8,-4,6,2],[1,3,7,5]]

def expensive_chessboard(T):
    n=len(T)
    F=[[0]*n for i in range(n)]

    F[0][0]=T[0][0]

    for i in range(1,n):
        F[0][i]=F[0][i-1]+T[0][i]
        F[i][0]=F[i-1][0]+T[i][0]

    for i in range(1,n):
        for j in range(1,n):
            F[i][j]=min(F[i-1][j]+T[i][j],F[i][j-1]+T[i][j])
    
    print(F)
    return F[n-1][n-1]


expensive_chessboard(K)

    