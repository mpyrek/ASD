class find_union:
    def __init__(self,val):
        self.val=val
        self.rank=0
        self.parent=self

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
        else:
            self.parent=N
            if self.rank==N.rank:
                N.rank=N.rank+1

