# python3

from queue import LifoQueue
from collections import namedtuple

stack=LifoQueue()





def find_mismatch(text):
    bracket=namedtuple('bracket',['character','position'])
    count=1
    m=0
    b=[]
    char=["(","[","{"]
    o_char=[")","]","}"]
    for i in text:
        s=bracket(i,count)
        #print(s.position)
        #print("i is as", i)
        if i in char:    
            stack.put(i)
            m=s.position
            b.append(m)
            
        elif i in o_char:
            if stack.empty():
                return s.position
            top=stack.get()
            b.pop()
            if (top=="(" and i!=")") or (top=="[" and i!="]") or (top=="{" and i!="}") :
                
                return s.position
        count+=1  
    if stack.empty()!= True :
        
        return b[0]
    return "Success"    
                
    

def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
