class find_union:
    def __init__(self,val):
        self.val=val
        self.rank=0
        self.parent=self
        self.min=val

    def find(self):
        if self!=self.parent:
            self.parent=self.parent.find()
        return self.parent

    def union(self,N):
        N=N.find()
        self=self.find()
        if self==N:
            return
        if N.rank < self.rank:
            N.parent=self
            self.min=min(N.min,self.min)
        else:
            self.parent=N
            N.min=min(N.min,self.min)
            if self.rank==N.rank:
                N.rank=N.rank+1

def equivalent_letters(A,B,C):
    T=[-1]*26

    for i in range(len(A)):
        if T[ord(A[i])-97]!=-1:
            if T[ord(B[i])-97]==-1:
                T[ord(B[i])-97]=find_union(B[i])
            T[ord(A[i])-97].union(T[ord(B[i])-97])
        else:
            T[ord(A[i])-97]=find_union(A[i])
            if T[ord(B[i])-97]==-1:
                T[ord(B[i])-97]=find_union(B[i])
            T[ord(B[i])-97].union(T[ord(A[i])-97])

    RES=[]    
    for i in range(len(C)):
        if T[ord(C[i])-97]!=-1:
            RES.append(T[ord(C[i])-97].parent.min)
        else:
            RES.append(C[i])
    
    for i in range(len(C)):
        print(RES[i])
    

A="abbd"
B="ccbd"
C="bcdab"
equivalent_letters(A,B,C)