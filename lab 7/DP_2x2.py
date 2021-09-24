S=[(1,2),(3,2),(1,4),(2,2)] #(W,P)

def count_posibilities(S,Max_w,Min_c):
    F=[]
    sum_profit=0
    for i in range(len(S)):
        sum_profit=sum_profit+S[i][1]

    for i in range(len(S)):
        F.append([])
        for j in range(Max_w+1):
            F[i].append([])
            for k in range(sum_profit):
                F[i][j].append(-1)
    
    
    F[0][0][0]=0
    F[0][S[0][0]][S[0][1]]=1
    count=0

    for i in range(1,len(S)):
        for j in range(Max_w+1):
            for k in range(sum_profit):
                F[i][j][k]=F[i-1][j][k]
                if j-S[i][0]>=0 and k-S[i][1]>=0 and F[i-1][j-S[i][0]][k-S[i][1]]!=-1:
                    F[i][j][k]=F[i][j][k]+1

    for i in range(Max_w+1):
        for j in range(Min_c,sum_profit):
            if F[len(S)-1][i][j]>=0:
                count=count+1
    print(count)

count_posibilities(S,3,3)

def count_posibilities2(S,Max_w,Min_c):
    F=[]

    for i in range(len(S)+1):
        F.append([])
        for j in range(Max_w+1):
            F[i].append([])
            for k in range(Min_c+1):
                F[i][j].append(-1)
    
    
    F[0][0][0]=0

    count=0

    for i in range(0,len(S)):
        for j in range(Max_w):
            for k in range(Min_c+1):
                if F[i][j][k]!=-1:
                    F[i+1][j][k]=F[i][j][k]
                    if j+S[i][0]<=Max_w:
                        if k+S[i][1]<Min_c:
                            F[i+1][j+S[i][0]][k+S[i][1]]=1
                        else:
                            F[i+1][j+S[i][0]][Min_c]=max(F[i+1][j+S[i][0]][Min_c]+1,1)
    print(F)
    for i in range(Max_w+1):
        if F[len(S)][i][Min_c]>=0:
            count=count+F[len(S)][i][Min_c]
    print(count)
count_posibilities2(S,3,3)