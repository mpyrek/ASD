import math

G=[1,7,2,5,1,1,3]

def find_max_2(T,a,b,span_a,span_b,idx,tmp_level,level):
    maks=-float('inf')
    def find_max(T,a,b,span_a,span_b,idx,tmp_level,level):
        nonlocal maks
        if a == span_a:
            if span_b<=b:
                maks=max(maks,T[idx])
            else:
                find_max(T,a,b,span_a,span_b-pow(2,level-tmp_level-1),2*idx+1,tmp_level+1,level)
                find_max(T,a,b,span_a+pow(2,level-tmp_level-1),span_b,2*idx+2,tmp_level+1,level)
        elif a>span_a:
            if span_b>span_a:
                find_max(T,a,b,span_a,span_b-pow(2,level-tmp_level-1),2*idx+1,tmp_level+1,level)
                find_max(T,a,b,span_a+pow(2,level-tmp_level-1),span_b,2*idx+2,tmp_level+1,level)
        elif a<span_a:
            if b>=span_b:
                maks=max(maks,T[idx])
            elif b<span_b and b>=span_a:
                find_max(T,a,b,span_a,span_b-pow(2,level-tmp_level-1),2*idx+1,tmp_level+1,level)
                find_max(T,a,b,span_a+pow(2,level-tmp_level-1),span_b,2*idx+2,tmp_level+1,level)
    
    find_max(T,a,b,span_a,span_b,idx,tmp_level,level)
    return maks



def make_tree(T):
    Tree=T[:]
    Tree.reverse()
    l1=0
    l2=len(Tree)

    while l2-l1>1:
        if (l2-l1)%2!=0:
            Tree.append(-float('inf'))
            l2=l2+1

        for i in range(l1,l2,2):
            x=max(Tree[i],Tree[i+1])
            Tree.append(x)
        l1=l2
        l2=len(Tree)

    Tree.reverse()
    return Tree

def find_max_3(T,a,b):
    Tree=make_tree(T)
    len_T=len(T)
    a=len(Tree)-len_T+a
    b=len(Tree)-len_T+b
    level=int(math.log2(len(Tree)))
    return find_max_2(Tree,a,b,pow(2,level)-1,pow(2,level)-1+pow(2,level)-1,0,0,level)

print(find_max_3(G,2,4))
