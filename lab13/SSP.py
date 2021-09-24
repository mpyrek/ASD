A=[-1,2,-15,1,2,10,-3,9,1,2,-21,1]

def SSP_1(T):
    results=0
    for i in range(len(T)):
        for j in range(i,len(T)):
            sum=0
            for k in range(i,j+1):
                sum+=T[k]
            results=max(sum,results)

    return results


def SSP_2(T):
    results=0
    for i in range(len(T)):
        sum=0
        for j in range(i,len(T)):
            sum+=T[j]
            results=max(sum,results)
    return results

    

def SSP_3(T,start,end):
    if end-start==0: return max(0,T[start])
    if end-start<0: return 0 
    mid=start+(end-start)//2
    sum_1=0
    sum_2=0
    max_1=0
    max_2=0

    for i in range(mid,start-1,-1):
        sum_1+=T[i]
        max_1=max(max_1,sum_1)

    for i in range(mid+1,end+1):
        sum_2+=T[i]
        max_2=max(max_2,sum_2)

    return max(SSP_3(T,start,mid),max_1+max_2,SSP_3(T,mid+1,end))

    


def SSP_4(T):
    results=[0]*len(T)
    results[0]=T[0]

    for i in range(1,len(T)):
        results[i]=max(results[i-1]+T[i],0)

    return max(results)


print(SSP_3(A,0,len(A)-1))
print(SSP_1(A))
print(SSP_2(A))
print(SSP_4(A))