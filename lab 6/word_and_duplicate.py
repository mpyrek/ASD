K="dcbabbdcbcbbd"
S2="ccbacdcbc"
def count_duplicate(S,duplicate):
    for i in range(len(S)):
        duplicate[ord(S[i])-97]=duplicate[ord(S[i])-97]+1
    


def the_smallest_word(S):
    duplicate=[0]*(122-97)
    count_duplicate(S,duplicate)
    
    Stack=[]
    curr_top=S[0]
    visted=[False]*(122-97)
    Stack.append(S[0])
    duplicate[ord(S[0])-97]=duplicate[ord(S[0])-97]-1
    visted[ord(S[0])-97]=True
    for i in range(1,len(S)):
        if curr_top>S[i] and duplicate[ord(curr_top)-97]>0:
            if Stack[len(Stack)-1]==curr_top:
                Stack.pop()
                duplicate[ord(S[i])-97]=duplicate[ord(S[i])-97]-1
                visted[ord(curr_top)-97]=False
                curr_top=S[i]
                visted[ord(S[i])-97]=True
                Stack.append(S[i])
            elif duplicate[ord(Stack[len(Stack)-1])-97]>0:
                while duplicate[ord(Stack[len(Stack)-1])-97]>1:
                    visted[ord(Stack.pop())-97]=False
                visted[ord(S[i])-97]=True
                Stack.append(S[i])
                duplicate[ord(S[i])-97]=duplicate[ord(S[i])-97]-1
                if Stack[0]==S[i]:
                    curr_top=S[i]
        elif visted[ord(S[i])-97]==False:
            if  duplicate[ord(Stack[len(Stack)-1])-97]>0 and S[i]<=Stack[len(Stack)-1]:
                while duplicate[ord(Stack[len(Stack)-1])-97]>0 and S[i]<=Stack[len(Stack)-1]:
                    visted[ord(Stack.pop())-97]=False
            visted[ord(S[i])-97]=True
            Stack.append(S[i])
            duplicate[ord(S[i])-97]=duplicate[ord(S[i])-97]-1
        

    while Stack:
        print(Stack.pop())
    
    

the_smallest_word(S2)