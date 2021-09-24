from copy import deepcopy
from collections import deque

def change_to_decimal(T):
  liczba=0
  for i in range(len(T)-1,-1,-1):
    liczba=liczba+T[i]*(2**(len(T)-i-1))
  return liczba

def change_to_binary(x,T):
  len_x=-1
  p=x
  while p!=0:
    p=p//2
    len_x=len_x+1
  for i in range(0,len(T)-len_x-1):
    T[i]=0
  for i in range(len(T)-1,len(T)-len_x-2,-1):
    T[i]=x%2
    x=x//2
  


def euler( G ):
  """miejsce na Twoją implementację!"""
  #WKW:
  n=len(G)
  flag=True
  for i in range(n):
    suma=0
    x=change_to_decimal(G[i])
    for j in range(n):
      suma=suma+G[i][j]
    if suma%2!=0:
          fla=False
    G[i][i]=x
  if flag==False:
    return None

  Q=deque() 
  O=[]
  visted=[False]*n
  def DFS_visit(i,n):
    nonlocal Q,O
    Q.append(i)
    if visted[i]==False:
      for j in range(n):
        if i!=j:
          if G[i][j]==1:
            G[i][j]=0
            G[j][i]=0
            DFS_visit(j,n)
        if j==n-1:
          O.append(Q.pop())
  DFS_visit(0,n)   
  for i in range(n):
    change_to_binary(G[i][i],G[i])
  return(O)
  
  
### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik
  
  
G = [[0,1,1,0,0,0],
     [1,0,1,1,0,1],
     [1,1,0,0,1,1],
     [0,1,0,0,0,1],
     [0,0,1,0,0,1],
     [0,1,1,1,1,0]]


GG = deepcopy( G )
cycle = euler( G )

if cycle == None: 
  print("Błąd (1)!")
  exit(0)
  
u = cycle[0]
for v in cycle[1:]:
  if GG[u][v] == False:
    print("Błąd (2)!")
    exit(0)
  GG[u][v] = False
  GG[v][u] = False
  u = v
  
for i in range(len(GG)):
  for j in range(len(GG)):
    if GG[i][j] == True:
      print("Błąd (3)!")
      exit(0)
      
print("OK")