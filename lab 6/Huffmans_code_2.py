from queue import PriorityQueue

S = ["a", "b", "c" ,"d", "e", "f" ]
F = [10 , 11 , 7 , 13, 1 , 20 ]

T=[0]*len(S)
suma=0

class Tree:
  def __init__(self,prob,char,idx=None):
    self.prob=prob
    self.char=char
    self.code=None
    self.right=None
    self.left=None
    self.idx=idx
  
  def __gt__(self, other):
    return self.prob > other.prob


  def __eq__(self, other):
    return self.prob == other.prob

  def get_marged_with(self,other):
   t=Tree(self.prob+other.prob,None)
   t.left=other
   t.right=self
   return t

  def calculate_code(self,code=[]):
    if self.char is not None:

      self.code=code[:]
    else:
      self.calculate_chlidreen_to_code(code)
      
  def calculate_chlidreen_to_code(self,code):
    self.calculate_child_to_code(code,self.left,0)
    self.calculate_child_to_code(code,self.right,1)


  def calculate_child_to_code(self,code,child,num):
    code.append(num)
    child.calculate_code(code)
    code.pop()

  def get_character(self):
    global T,suma

    if self.char is not None:
      T[self.idx]=(self.char,self.code)
      suma=suma+len(self.code)*self.prob
    else:
      if self.left:
        self.left.get_character()
        self.right.get_character()


def huffman( S, F ):

  """miejsce na Twoją implementację!"""

  Q=PriorityQueue()
  for i in range(len(F)):
    Q.put(Tree(F[i],S[i],i))
  

  trie=Q.get()
  while not Q.empty():
    root=trie.get_marged_with(Q.get())
    Q.put(root)
    trie=Q.get()

  root.calculate_code()
  root.get_character()

  for i in range(len(S)):
    print(T[i])

  print(suma)
  
  pass



huffman( S, F )