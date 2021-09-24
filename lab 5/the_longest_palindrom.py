#najdluzszy palindrom w ciagu
#if i=j F[i][j]=max(F[i][j],F[i-1][j-1]+1)

#do sprawdzenia

def print_solution(A,F,idx_of_max):
    if F[idx_of_max[0]][idx_of_max[1]]==1:
        print(A[idx_of_max[1]],end='')
    else:
        print_solution(A,F, (idx_of_max[0]-1,idx_of_max[1]-1))
        print(A[idx_of_max[1]],end='')




def count_length(A):
    n=len(A)

    F=[[0]*n for i in range(n)]

    idx_of_max=0

    max_len=0

    for i in range(len(A)):

        if A[i]==A[n-1]:
            F[0][i]=1
            idx_of_max=(0,i)
            max_len=0
        if A[0]==A[n-i-1]:
            F[i][0]=1


    for i in range(1,len(A)):
        for j in range(1,len(A)):
            #A[n-i-1]-odwrócony ciąg, A[i]-normlany ciąg
            if A[n-i-1]==A[j]:
                if F[i][j]<F[i-1][j-1]+1:
                    F[i][j]=F[i-1][j-1]+1

                    if F[i][j]>max_len:
                        idx_of_max=(i,j)
                        max_len=F[i][j]


    print_solution(A, F, idx_of_max)
    print("")
    return max_len
                    
                


S="abbabab"

print(count_length(S))