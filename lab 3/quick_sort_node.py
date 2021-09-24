from random import randint, seed


class Node:
  def __init__(self):
    self.next = None
    self.value = None
    

class List:
    def __init__(self):
        self.head=None
        self.tail=None

    def push(self,w):
        N=Node()
        N.value=w
        if self.head==None:
            self.head=N
            self.tail=N
        else:
            self.tail.next=N
            self.tail=N

    def is_empty(self):
        return self.head==None

    def print_list(self):
        h=self.head
        while h:
            print(h.value)
            h=h.next



def qsort(L):

    def make_list(L):
        L1=List()
        L1.head=L
        L1.tail=L

        while L.next:
            L=L.next
            L1.tail=L
        return L1


    def glue_two_l(L,R):
        if L.is_empty():
           return R
        if R.is_empty():
           return L

        L.tail.next=R.head
        L.tail=R.tail

        return L


    def q_sort(L):
        if L.is_empty()==True:
           return L

        pivot=L.head.value
        lT=List()   #el. mniejsze od pivot
        gT=List()   #el. większe od pivot
        eqT=List()   #el. równe pivot
        l=L.head
 
        while l:
            if l.value<pivot:
                lT.push(l.value)
            elif l.value>pivot:
                gT.push(l.value)
            else:
                eqT.push(l.value)
            l=l.next    
    
        return glue_two_l(glue_two_l(q_sort(lT),eqT),q_sort(gT))


    L=make_list(L)
    L=q_sort(L).head
    return L 
   


def tab2list( A ):
  H = Node()
  C = H
  for i in range(len(A)):
    X = Node()
    X.value = A[i]
    C.next = X
    C = X
  return H.next
  
  
def printlist( L ):
  while L != None:
    print( L.value, "->", end=" ")
    L = L.next
  print("|")

 
  

seed(42)

n = 10
T = [ randint(1,10) for i in range(10) ]
L = tab2list( T )

print("przed sortowaniem: L =", end=" ")
printlist(L) 

L = qsort(L)
print("po sortowaniu    : L =", end=" ")
printlist(L)

if L == None:
  print("List jest pusta, a nie powinna!")
  exit(0)

P = L
while P.next != None:
  if P.value > P.next.value:
    print("Błąd sortowania")
    exit(0)
  P = P.next
    
print("OK")

