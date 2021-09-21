class Node:
    def __init__(self,val):
        self.next=None
        self.val=val


T=[2,3,1,7,2,6,2,5]
for i in range(len(T)):
    T[i]=Node(T[i])

for i in range(len(T)-1):
    T[i].next=T[i+1]



def split(Li):
    lenn=0
    h=Li
    while h:
        h=h.next
        lenn=lenn+1
    
    lenn=lenn-1
    head1=Li
    lenn=lenn//2
    
    while lenn>0:
        Li=Li.next
        lenn=lenn-1
    
    head2=Li.next
    Li.next=None

    return(head1,head2)

def merge(L1,L2):
    if L1.val<=L2.val:
        head=L1
        L1=L1.next
    else:
        head=L2
        L2=L2.next

    #trzymamy głowę
    h=head

    while L1 and L2:
        if L1.val<=L2.val:
            head.next=L1
            L1=L1.next
        else:
            head.next=L2
            L2=L2.next
        head=head.next

    while L1:
        head.next=L1
        L1=L1.next
        head=head.next

    while L2:
        head.next=L2
        L2=L2.next
        head=head.next

    return h


def merge_sort(Li):
    if Li.next:
        l1,l2 = split(Li)
        l1 = merge_sort(l1)
        l2 = merge_sort(l2)

        Li=merge(l1,l2)

    return Li
        

T[0]=merge_sort(T[0])

while T[0]:
    print(T[0].val)
    T[0]=T[0].next







