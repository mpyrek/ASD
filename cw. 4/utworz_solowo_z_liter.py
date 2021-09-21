A="ania"
B="zaga"
C="nagaz"

def counting__letter(T,F):

    for i in range(len(T)):
        idx=ord(T[i])-97
        F[idx]=F[idx]+1

    return F


def is_posible(A,B,C):
    F=[0]*26
    counting__letter(A,F)
    counting__letter(B,F)

    for i in range(len(C)):
        idx=ord(C[i])-97
        F[idx]=F[idx]-1
        if F[idx]<0:
            return False
    return True
print(is_posible(A,B,C))
