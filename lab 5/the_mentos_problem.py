#Dostajemy listę wartości. Gramy z drugim graczem. Wybieramy zawsze jedną wartość z jednego z końców tablicy i dodajemy do swojej sumy, a następnie to samo robi nasz przeciwnik. Zakładając, że przeciwnik gra optymalnie, jaką maksymalną sumę możemy uzbierać?  
#“Uogólniony problem paczki mentosów”

A=[2,2,5,3,3]

#F[i,j]-max suma jak grasz może uzbierać po i ruchach 
def mentos_problem(T):
    n=len(T)
    F=[[0]*n for i in range(n)]
    S=[[0]*n for i in range(n)]

    for i in range(n):
        #uzupełniamy przekątną
        F[i][i]=T[i]
        S[i][i]=T[i]

    for k in range(1,n):
        for i in range(k,n):
            #zlicza sume od i-k do i w T
            S[i][i-k]=S[i-1][i-k]+T[i]
            #max wartość jaką mozemy uzyskać mając do dyspozycji of i-k do k mentosów suma T[i-k:i] -minimum jakie pozostawimy przeciwnikiowi
            F[i][i-k]=S[i][i-k]-min(F[i-1][i-k],F[i][i-k+1])

  #  for i in range(n):
   #     for j in range(n):
    #        print(F[i][j],end=' ')
     #   print(" ")

    print(F[n-1][0])

#geeks dla porównanie wyników
def optimalStrategyOfGame(arr, n):
     
    # Create a table to store
    # solutions of subproblems
    table = [[0 for i in range(n)]
                for i in range(n)]
 
    # Fill table using above recursive
    # formula. Note that the table is
    # filled in diagonal fashion
    # (similar to http://goo.gl / PQqoS),
    # from diagonal elements to
    # table[0][n-1] which is the result.
    for gap in range(n):
        for j in range(gap, n):
            i = j - gap
             
            # Here x is value of F(i + 2, j),
            # y is F(i + 1, j-1) and z is
            # F(i, j-2) in above recursive
            # formula
            x = 0
            if((i + 2) <= j):
                x = table[i + 2][j]
            y = 0
            if((i + 1) <= (j - 1)):
                y = table[i + 1][j - 1]
            z = 0
            if(i <= (j - 2)):
                z = table[i][j - 2]
            table[i][j] = max(arr[i] + min(x, y),
                              arr[j] + min(y, z))
    return table[0][n - 1]

arr1 = [ 8, 15, 3, 7 ]
n = len(arr1)
print(optimalStrategyOfGame(arr1, n))
mentos_problem(arr1)

arr2 = [ 2, 2, 2, 2 ]
n = len(arr2)
print(optimalStrategyOfGame(arr2, n))
mentos_problem(arr2)
 
arr3 = [ 20, 30, 2, 2, 2, 10]
n = len(arr3)
print(optimalStrategyOfGame(arr3, n))
mentos_problem(arr3)

mentos_problem(A)
print(optimalStrategyOfGame(A, len(A)))