#Dana jest tablica n liczb naturalnych A. Liczba A[i] mówi ile razy i-ty symbol pojawia się w tekście. Proszę zaimplementować funkcję huffman len(A), która oblicza ile bitów zajęłoby zapisanie tekstu składającego się właśnie z takiej liczby symboli, jeśli użytoby optymalnego kodu Huffmana. Funkcja powinna działać w czasie O(n log n). Podpowiedź: Może się przydać struktura kopca.
#Państwa kod powinien mieć następującą postać (będzie uruchamiany; proszę nieusuwać fragmentu testującego; sprawdzający może także dołożyć swoje testy):
#def huffman_len(A):
# tu proszę umieścić swoją implementację
# elementarny test, powinien wypisać 2600
#print( huffman_len([ 200, 700, 180, 120, 70, 30] )

A=[200,700,180,120,70,30]

import math

class Heap:
	def __init__(self,oper=lambda x,y: x<y):
		self.tab=[0]
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
		if self.len()==0: return None
		return self.tab[1]

	def heapify(self,i):
		size=self.len()
		l=self.l(i)
		r=self.r(i)
		tab=self.tab

		idx=i
		if l<=size and self.oper(tab[l],tab[idx]):
			idx=l
		if r<=size and self.oper(tab[r],tab[idx]):
			idx=r
		if idx==i: return
		tab[i],tab[idx]=tab[idx],tab[i]
		self.heapify(idx)
	
	def make_heap(self,tab):
		size=len(tab)
		self.tab=[size]+tab
		for i in range(size//2,0,-1):
			self.heapify(i)
	
	def heapify_up(self,i):
		p=self.p(i)
		if p<1: return
		tab=self.tab

		if self.oper(tab[i],tab[p]):
			tab[i],tab[p]=tab[p],tab[i]
		if i==2*p+1 and tab[2*p+1]<tab[2*p]:
			tab[i],tab[i-1]=tab[i-1],tab[i]
		self.heapify_up(p)
	
	def push(self,x):
		self.tab.append(x)
		self.tab[0]=self.tab[0]+1
		self.heapify_up(self.tab[0])

	def pop_top(self):
		size=self.len()
		top=self.get_top()
		self.tab[1]=self.tab[size]
		self.tab.pop()
		self.tab[0]-=1
		self.heapify(1)
		return top

# a teraz drzewo

class Node:
	def __init__(self, prob, character=None):
		self.prob = prob
		self.character = character
		self.code = None
		self.left = None
		self.right = None

	def get_merged_with(self, other):
		merged = Node(other.prob + self.prob)
		merged.left = self
		merged.rigth = other
		return merged

	def __lt__(self, rhs):
		return self.prob < rhs.prob
 
	def calculate_codes(self, code=[]):
		if self.character is not None:
			self.code = code[:]
		else:
			self._calculate_codes_to_children(code)
 
	def _calculate_codes_to_children(self, code):
		if self.left is not None:
			self._calculate_code_to_child(code, self.left, 0)
			self._calculate_code_to_child(code, self.rigth, 1)
	
	def _calculate_code_to_child(self, code, child, num):
		code.append(num)
		child.calculate_codes(code)
		code.pop()

	def get_characters_with_codes(self):
		if self.character is not None:
			return {self.character: self.code}
		else:
			return self._get_characters_with_codes_of_children()
	
	def _get_characters_with_codes_of_children(self):
		return dict(self.left.get_characters_with_codes, **self.right.get_characters_with_codes)


def huffman_len(A):
	heap1=Heap()
	tab=[Node(el,1) for el in A]
	heap1.make_heap(tab)
	
	#stworzyć heapa 
	while heap1.len()!=1:
		trie=heap1.pop_top()
		root=trie.get_merged_with(heap1.pop_top())
		heap1.push(root)

	root.calculate_codes()

huffman_len(A)