
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

L=make_list(G)



def select_sort(head):
    
    #ogarniamy głowę
    item=head
    pointer_of_min=None
    while item.next!=None:
        if item.next.val<head.val:
            if pointer_of_min==None or pointer_of_min.next.val>item.next.val:
                pointer_of_min=item
        item=item.next
    
    h=head.next
    head.next=None
    x=pointer_of_min.next
    next=pointer_of_min.next.next
    pointer_of_min.next=head
    head.next=next
    x.next=h
    head=x

    head.print_list()
    
    prev=head
    item=head

    while prev.next!=None:
        pointer=item
        while item.next!=None:
            if item.next.val<pointer.next.val:
                pointer=item
            item=item.next
        x=pointer.next
        z=pointer.next.next
        y=prev.next.next
        if pointer.next!=prev.next:
            pointer.next=prev.next
        prev.next.next=z
        prev.next=x
        x.next=y
        prev=x
        item=prev

        
        
    

def selectionSort(head):
     
    temp = head
    # Traverse the List
    while temp:
         
        minn = temp
        r = temp.next
         
        # Traverse the unsorted sublist
        while r:
            if minn.val > r.val:
                minn = r
             
            r = r.next
             
        # Swap val
        x = temp.val
        temp.val = minn.val
        minn.val = x
        temp = temp.next



selectionSort(L)
L.print_list()