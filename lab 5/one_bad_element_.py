class Node:
    def __init__(self,val):
        self.next=None
        self.val=val

A=Node(8)
B=Node(2)
C=Node(3)
D=Node(4)
E=Node(6)
F=Node(7)
G=Node(9)
H=Node(10)
A.next=B
B.next=C
C.next=D
D.next=E
E.next=F
F.next=G
G.next=H


def fix_list(head):
    #sprawdzamy głowę
    if head.val>head.next.val:
        h=head.next
        h_1=head.next
        while h.next and h.next.val<head.val:
            h=h.next
        tmp=h.next
        h.next=head
        head.next=tmp
        head=h_1
    else:
        h=head
        while h.next.next and h.next.val<h.next.next.val:
            h=h.next
        if h.val<h.next.next.val:
            tmp=h.next
            h.next=h.next.next
        else:
            tmp=h.next.next
            h.next.next=h.next.next.next
        h=head
        while h.next and h.next.val<tmp.val:
            h=h.next
        x=h.next
        h.next=tmp
        tmp.next=x
    return head


h=fix_list(A)
while h:
    print(h.val)
    h=h.next