#Dany jest graf nieskierowany G = (V,E) z ważonymi krawędziami (w: E -> N). Proszę zaproponować jak najszybszy algorytm, który znajduje ścieżkę z danego wierzchołka s do danego wierzchołka t taką, że:
#Każda kolejne krawędź ma mniejszą wagę niż poprzednia
#Spośród ścieżek spełniających powyższy warunek, znaleziona ma najmniejszą sumę wag

#zlożonosć |v|*log(|v|)+ Elog(V) lub V^2
#V-ilość wierzchołków , |v|-dag(v)

from queue import PriorityQueue

#kopiec typu min
class Heap:
	def __init__(self, oper=lambda x, y: x < y):
		self.tab = [0]
		self.oper=oper
	
	def l(self,i):
		return 2*i

	def r(self,i):
		return 2*i+1

	def p(self,i):
		return i//2

	def len(self):
		return self.tab[0]

	def get_top(self):
		if self.len()==0:
			return None
		return self.tab[1]

	def heapify(self,i):
		size=self.len()
		tab=self.tab
		l=self.l(i)
		r=self.r(i)

		idx=i
		if l<=size and self.oper(tab[l][0],tab[idx][0]):
			idx=l
		if r<=size and self.oper(tab[r][0],tab[idx][0]):
			idx=r
		if idx == i:
			return
		tab[idx], tab[i] = tab[i], tab[idx]
		self.heapify(idx)


	def bulid_heap(self, tab):
		size=len(tab)
		self.tab=[size] + tab
		for i in range(size // 2, 0, -1):
			self.heapify(i)
	
	def pop_top(self):
		size=self.len()
		top=self.get_top()
		self.tab[1]=self.tab[size]
		self.tab.pop()
		self.tab[0]=self.tab[0]-1
		self.heapify(1)
		return top

	def heapify_up(self,i):
		p=self.p(i)
		if p<1:
			return
		tab=self.tab
		if self.oper(tab[i][0],tab[p][0]):
			tab[i],tab[p] = tab[p],tab[i]
			self.heapify_up(p)


	def push(self,w):
		self.tab.append(w)
		self.tab[0] = self.tab[0]+1 
		self.heapify_up(self.len())

	def heapsort(self,tab):
		self.bulid_heap(tab)
		for i in range(self.len(),0,-1):
			tab[i-1]=self.pop_top() 
		return tab

class V:
    def __init__(self):
        self.parent=None
        self.queue=Heap()
        

L=[[[1,10],[2,5]],[[0,10],[3,8],[6,12]],[[0,5],[3,4],[4,3]],[[1,8],[2,4],[6,7]],[[2,3],[5,2]],[[4,2],[6,11]],[[1,12],[3,7],[5,11],[7,2]],[[6,2]]]

def print_solution(v,s,T):
    if T[v].parent!=s:
        print_solution(T[v].parent,s,T)
    print(v,end=', ')

def find_path(G,s,t):
    T=[0]*len(G)
    for i in range(len(G)):
        T[i]=V()

    for i in range(len(G)):
        for el in G[i]:
            T[i].queue.push((el[1],el[0]))
    
    Q=PriorityQueue()
    #dist, waga_ostatnia, idx
    Q.put((0,float('inf'),s))

    while Q.empty()==False:
        dist, w, idx=Q.get()
        if idx==t and T[idx].parent!=None:
            print(s,end=', ')
            print_solution(idx,s,T)
            print()
            return(dist)
            
        
        while T[idx].queue.len()!=0  and T[idx].queue.get_top()[0] <w:
            wage,x=T[idx].queue.pop_top()
            T[x].parent=idx
            Q.put((wage+dist,wage,x))
    
    return None


def find_path_2(G,s,t):
	T=[0]*len(G)
	for i in range(len(G)):
		T[i]=V()

	for i in range(len(G)):
		for j in range(len(G)):
			if G[i][j] != float('inf'):
				T[i].queue.push((G[i][j],j))
    
	Q=PriorityQueue()
    #dist, waga_ostatnia, idx
	Q.put((0,float('inf'),s))

	while Q.empty()==False:
		dist, w, idx=Q.get()
		if idx==t and T[idx].parent!=None:
			print(s,end=', ')
			print_solution(idx,s,T)
			print()
			return(dist)

		while T[idx].queue.len()!=0  and T[idx].queue.get_top()[0] <w:
			wage,x=T[idx].queue.pop_top()
			T[x].parent=idx
			Q.put((wage+dist,wage,x))
    
	return None



G_M=[[float('inf'),10,5,float('inf'),float('inf'),float('inf'),float('inf'),float('inf')],
	[10,float('inf'),float('inf'),8,float('inf'),float('inf'),12,float('inf')],
	[5,float('inf'),float('inf'),4,3,float('inf'),float('inf'),float('inf')],
	[float('inf'),8,4,float('inf'),float('inf'),float('inf'),7,float('inf')],
	[float('inf'),float('inf'),3,float('inf'),float('inf'),2,float('inf'),float('inf')],
	[float('inf'),float('inf'),float('inf'),float('inf'),2,float('inf'),11,float('inf')],
	[float('inf'),12,float('inf'),7,float('inf'),11,float('inf'),2],
	[float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),2,float('inf')]
]


print(find_path(L,0,6))
print(find_path_2(G_M,0,6))


#----TEST A----
G_1 = [
    [(1, 10), (2, 5)], # 0
    [(0, 10), (3, 8), (6, 12)], # 1
    [(0, 5), (3, 4), (4, 3)],   # 2
    [(1, 8), (2, 4), (6, 7)],   # 3
    [(2, 3), (5, 2)],   # 4
    [(4, 2), (6, 11)],   # 5
    [(1, 12), (3, 7), (5, 11), (7, 2)], # 6
    [(6, 2)]    # 7
]
# results:
# 0 —> 7 (27) path: [0, 1, 3, 6, 7]
# 1 —> 2 (12) path: [1, 3, 2]
# 5 —> 2 (22) path: [5, 6, 3, 2]
# 2 —> 7 (None)


#print(find_path(G_1,0,7))
#print(find_path(G_1,1,2))
#print(find_path(G_1,5,2))
#print(find_path(G_1,2,7))

#----TEST B----
G_2 = [
    [(1, 6), (6, 2)],
    [(5, 5), (2, 5)],
    [(3, 2), (4, 3)],
    [],
    [(7, 4), (8, 2)],
    [(2, 4), (6, 3), (7, 3)],
    [(0, 2), (7, 2), (8, 5)],
    [],
    []
]
# results:
# 0 —> 0 (16) 0, 1, 5, 6, 0, 
# 0 —> 8 (16) path: [0, 1, 2, 4, 8]
# 1 —> 8 (10) path: [1, 2, 4, 8]
# 7 —> 4 (None)


#print(find_path(G_2,0,0))
#print(find_path(G_2,0,8))
#print(find_path(G_2,1,8))
#print(find_path(G_2,7,4))


#----TEST C----
G_3 = [
    [(1, 4), (4, 8)],
    [(4, 3)],
    [(3, 3)],
    [],
    [(7, 2), (5, 4)],
    [(2, 1), (3, 5)],
    [(4, 10)],
    []
]
# results:
# 0 —> 2 (12) path: [0, 1, 4, 5, 2]
# 0 —> 7 (9) path: [0, 1, 4, 7]
# 5 —> 0 (None)


#print(find_path(G_3,0,2))
#print(find_path(G_3,0,7))
#print(find_path(G_3,5,0))

#----TEST D----
G_4 = [
    [],
    [(3, 1), (5, 12), (2, 2)],
    [],
    [(2, 3), (4, 4)],
    [(5, 5)],
    []
]
# results:
# 3 —> 4 (4) path: [3, 4]
# 1 —> 5 (12) path: [1, 5]
# 1 —> 2 (2) path: [1, 2]

#print(find_path(G_4,3,4))
#print(find_path(G_4,1,5))
#print(find_path(G_4,1,2))