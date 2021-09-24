from typing import final


A="ababbabaabbab"

class Node:
    def __init__(self):
        self.left=None
        self.right=None
        self.val=0

class Tree:
    def __init__(self):
        self.root=Node()
        

    def push(self,str,k):
        self=self.root

        for i in range(k):
            if str[i]=='a':
                if self.left==None:
                    self.left=Node()
                    self=self.left
                else:
                    self=self.left
            else:
                if self.right==None:
                    self.right=Node()
                    self=self.right
                else:
                    self=self.right

        self.val=self.val+1
        return self.val


def count(T,k):
    Tr=Tree()
    max=0
    max_str=""
    for i in range(len(T)-k):
        tmp_m=Tr.push(T[i:i+k],k)
        if max<tmp_m:
            max=tmp_m
            max_str=T[i:i+k]
    return max_str
                        
print(count(A,3))         


def find_the_most_repeted(T,k):
    maxi=0
    best_sub=0
    Res=[0]*pow(2,k)

    for i in range(len(T)-k):
        idx=0
        for j in range(k):
            if T[i+j]=='a':
                idx=idx*2+1
            else:
                idx=idx*2+2
        idx=idx-pow(2,k)-1
        Res[idx]=Res[idx]+1
        if Res[idx]>maxi:
            maxi=Res[idx]
            best_sub=T[i:i+k]
    return best_sub

print(find_the_most_repeted(A,3))

