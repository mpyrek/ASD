# problem sumy podzbiorów 

import math



def find_sum_2(T,a,b,span_a,span_b,idx,tmp_level,level):
    sum=0
    def find_sum(T,a,b,span_a,span_b,idx,tmp_level,level):
        nonlocal sum 
        if a == span_a:
            if span_b<=b:
                sum=sum+T[idx]
            else:
                find_sum(T,a,b,span_a,span_b-pow(2,level-tmp_level-1),2*idx+1,tmp_level+1,level)
                find_sum(T,a,b,span_a+pow(2,level-tmp_level-1),span_b,2*idx+2,tmp_level+1,level)
        elif a>span_a:
            if span_b>span_a:
                find_sum(T,a,b,span_a,span_b-pow(2,level-tmp_level-1),2*idx+1,tmp_level+1,level)
                find_sum(T,a,b,span_a+pow(2,level-tmp_level-1),span_b,2*idx+2,tmp_level+1,level)
        elif a<span_a:
            if b>=span_b:
                sum=sum+T[idx]
            elif b<span_b and b>=span_a:
                find_sum(T,a,b,span_a,span_b-pow(2,level-tmp_level-1),2*idx+1,tmp_level+1,level)
                find_sum(T,a,b,span_a+pow(2,level-tmp_level-1),span_b,2*idx+2,tmp_level+1,level)
    
    find_sum(T,a,b,span_a,span_b,idx,tmp_level,level)
    return sum



def make_tree(T):
    Tree=T[:]
    Tree.reverse()
    l1=0
    l2=len(Tree)

    while l2-l1>1:
        if (l2-l1)%2 != 0:
            Tree.append(0)
            l2=l2+1
        for i in range(l1,l2,2):
            Tree.append(Tree[i]+Tree[i+1])
        l1=l2
        l2=len(Tree)

    Tree.reverse()
    return Tree
    

def span_sum_Tree(Tree,a,b,len_T):
    a=len(Tree)-len_T+a
    b=len(Tree)-len_T+b

    level=int(math.log2(len(Tree)))
    return find_sum_2(Tree,a,b,pow(2,level)-1,pow(2,level)-1+pow(2,level)-1,0,0,level)
    
    
#zamieniamy to co pod indeksem a na wartość b
def change_el_a_to_b(Tree,a,b,len_T):
    idx=len(Tree)-len_T+a
    ods=Tree[idx]-b
    Tree[idx]=b
    idx=(idx-1)//2

    if ods!=0:
        while idx!=0:
            Tree[idx]=Tree[idx]-ods
            idx=(idx-1)//2
    return Tree
        
    
Tree=make_tree(G)
print(span_sum_Tree(Tree,1,6,len(G)))
change_el_a_to_b(Tree,1,10,len(G))
print(span_sum_Tree(Tree,1,6,len(G)))