#Domknięciem przechodnim skierowanego grafu G = (V, E) nazywamy taki graf G0 = (V, E0), że dla każdych dwóch wierzchołków u, v ∈ V graf G0 ma krawędź z u do v wtedy i tylko wtedy, gdy w G jest skierowana ścieżka z u do v. Proszę zaimplementować funkcję tclosure( G ), która na wejście otrzymuje graf skierowany w reprezentacji macierzowej (bez wag; G[i][j] to wartość logiczna mówiąca czy istnieje krawędź z i do j) i zwraca graf będący domknięciem przechodnim G (w tej samej reprezentacji).
# Państwa kod powinien mieć następującą postać (będzie uruchamiany; proszę nie usuwać fragmentu testującego; sprawdzający może także dołożyć swoje testy):



def tclosure( G ):   
# policz domknięcie przechodnie G i je zwróc
    n=len(G)

    for t in range(n):
        for j in range(n):
            for i in range(n):
                if G[i][j]!=1 and G[i][t]==1 and G[t][j]==1:
                    G[i][j]=1

    return(G)


G = [ [0, 1 , 0],
[0, 0, 1 ],
[0, 0, 0] ]
#print( tclosure( G ) ) 
# [[False, True , True],
# [False, False, True],
# [False, False, False]]

G_2 = [
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

#print( tclosure( G_2 ) ) 

G_3=[[0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0]]

print( tclosure( G_3 ) ) 