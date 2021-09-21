#W szeregu ustawiło się 2n żołnierzy. Połowa z nich to zwykli szeregowi, a połowa to siły specjalne. Mieli się ustawić na 2 grupy: najpierw szeregowi, a potem specjalni, ale sierżant zapomniał im o tym powiedzieć. Stoją teraz przypadkowo, z odstępem 1 metra pomiędzy kolejnymi żołnierzami. Szereg to lista struktur typu:

class Soldier:
    type = False  # is a special soldier?
    next = None
#Zaimplementuj funkcję distanceToIdeal(firstSoldier), która oblicza najmniejszą liczbę metrów, jaką żołnierze muszą sumarycznie przejść, żeby szeregowi stali po lewej od żołnierzy specjalnych (i żeby cały szereg dalej stał w tym samym miejscu).
#Uwaga: nie wymaga się sortowania listy.

T=[None]*8

for i in range(len(T)):
    T[i]=Soldier()

for i in range(len(T)-1):
    T[i].next=T[i+1]

T[0].type=True
T[3].type=True
T[4].type=True
T[7].type=True


def print_list(head):
    h=head
    while h:
        print(h.type)
        h=h.next


def distanceToIdeal(firstSoldier):
    pointer_1=firstSoldier
    pointer_2=firstSoldier

    #liczymy dłg
    len=0
    while pointer_1!=None:
        pointer_1=pointer_1.next
        len=len+1

    #dalej wskazuje na head
    pointer_1=pointer_2

    #idziemy do połowy
    l=len//2
    while l!=1:
        pointer_2=pointer_2.next
        l=l-1
    #false na lewo true na prawo
    l=len//2
    distance=0

    while pointer_2.next and pointer_2.next.type:
        pointer_2=pointer_2.next
 

distanceToIdeal(T[0])




    
