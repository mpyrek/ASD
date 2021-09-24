class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

    def print_list(self):
        while self:
            print(self.val)
            self=self.next


G=[4,2,7,3,6,5,1]

def make_list(T):
    for i in range(len(T)):
        T[i]=Node(T[i])

    for i in range(len(T)-1):
        T[i].next=T[i+1]
    return T[0]



def change_way(head):
    prev=None
    item=head

    while item:
        next=item.next
        item.next=prev
        prev=item
        item=next

    return prev
    
G=[4,2,7,3,6,5,1]
L=make_list(G)

L.print_list()
L=change_way(L)
print("zmiana")
L.print_list()
    