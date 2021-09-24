#rozdzielmy dwie listy bez wartownika na przyste i nieparzyste
class Node:
    def __init__(self,val):
        self.next=None
        self.val=val

A=Node(2)
B=Node(3)
C=Node(1)
D=Node(4)
E=Node(11)
F=Node(13)
G=Node(6)
H=Node(1)
I=Node(2)

A.next=B
B.next=C
C.next=D
D.next=E
E.next=F
F.next=G
G.next=H
H.next=I

def split(head):
    head_odd=None
    head_even=None
    if head.val%2==1:
        head_odd=head
        head=head.next
        h_o=head_odd
        while head.val%2==1:
            h_o.next=head
            h_o=h_o.next
            head=head.next
    else:
        head_even=head
        head=head.next
        h_e=head_even
        while head.val%2==0:
            h_e.next=head
            h_e=h_e.next
            head=head.next

    if head_even==None:
        head_even=head
        h_e=head_even
        head=head.next
    else:
        head_odd=head
        h_o=head_odd
        head=head.next
        
    while head:
        if head.val%2==0:
            h_e.next=head
            h_e=h_e.next
        else:
            h_o.next=head
            h_o=h_o.next
        head=head.next

    h_e.next=None
    h_o.next=None
    return ((head_even,head_odd))


h1,h2=split(A)
while h1:
    print(h1.val)
    h1=h1.next

print("nowe")
while h2:
    print(h2.val)
    h2=h2.next

