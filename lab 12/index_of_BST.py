#Zadanie 1. (Indeksowane drzewa BST) Rozważmy drzewa BST, które dodatkowo w każdym węźle zawierają pole z liczbą węzłów w danym poddrzewie. Proszę opisać jak w takim drzewie wykonywać
#następujące operacje:
#1. znalezienie i-go co do wielkości elementu,
#2. wyznaczenie, którym co do wielkości w drzewie jest zadany węzeł


class BSTNode:
    def __init__(self):
        self.key = None
        self.left = None
        self.right = None
        self.parent = None
        self.nodes_l=None


def search(S,key):
    x=S.root
    while x!=None:
        if x.key==key:
            return x
        elif x.key>key:
            x=x.left
        else:
            x=x.right
    return None


def minimum(N):
    while N.left!=None:
        N = N.left
    return N
    
def maximum(N):
    while N.right!=None:
        N =N.right
    return N


def prev(N):
    if N.left!=None:
        return maximum(N.left)
    else:
        while N.parent!=None and N.parent.right!=N:
            N=N.parent
        return N.parent


def next(N):
    if N.right!=None:
        return minimum(N.right)
    else:
        while N.parent!=None and N.parent.left!=N:
            N=N.parent
        return N.parent

    
def print_BST(N):
    if N!=None:
        if N.left:
            print_BST(N.left)
        print(N.key,N.nodes_l,end=', ')
        if N.right:
            print_BST(N.right)


def insert(S,key):
    if search(S,key)!=None:
        return False
    else:
        y=None
        x=S.root
        N=BSTNode()
        N.key=key

        while x!=None:
            y=x
            if x.key > key:
                x.nodes_l=x.nodes_l+1
                x=x.left
            else:
                x=x.right

                
        N.parent=y
        N.nodes_l=0
        if y==None:
            S.root=N
        elif y.key > key:
            N.root=S.root
            y.left=N
        else:
            N.root=S.root
            y.right=N
            
        return True
        

    #key
def remove(S,key):
    N=search(S,key)
    if N==None:
        return False
    else:
        if N.left==None and N.right==None:
            if N.parent!=None:
                if N.parent.left==N:
                    N.parent.left=None
                else:
                    N.parent.right=None
                N.parent=None
            else:
                S.root=None
                
    
            
        elif N.left!=None and N.right==None:
            if N.parent!=None:
                if N.parent.left==N:
                    N.parent.left=N.left
                else:
                    N.parent.right=N.left
                N.left.parent=N.parent
            else:
                N.left.parent=None
                x=N.left
                S.root=x
                
    
        elif N.left==None and N.right!=None:
            if N.parent!=None:
                if N.parent.right==N:
                    N.parent.right=N.right
                else:
                    N.parent.left=N.right
                N.right.parent=N.parent
            else:
                N.right.parent=None
                x=N.right
                N.right=None
                S.root=x
                
        
        else:
            x=prev(N).key
            remove(S,x)
            N.key=x


def find_k_el(N,k):
    if N:
        if k-1==N.nodes_l:
            return N
        elif N.nodes_l >= k:
            return find_k_el(N.left,k)
        else:
            return find_k_el(N.right,k-N.nodes_l-1)
            
    return None 


def which_node(S,N):
    counter=1
    while S!=N:
        if S.key > N.key:
            S=S.left  
        else:
            counter= counter + 1
            counter = counter+S.nodes_l
            S=S.right
    
    return counter+S.nodes_l


class BST(BSTNode):
    def __init__(self):
        self.root=None
        


S=BST()
insert(S,15)
insert(S,6)
insert(S,3)
insert(S,7)
insert(S,2)
insert(S,4)
insert(S,13)
insert(S,9)
insert(S,18) 
insert(S,17)
insert(S,20)
print_BST(S.root)
print("")
#x=find_k_el(S.root,5)
y=which_node(S.root,S.root.left.left.left)
print(y)