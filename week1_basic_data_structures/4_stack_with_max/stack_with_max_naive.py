import sys
from collections import deque
class findMaximum:
    def __init__(self):
        self.stack=deque()
        self.maximum=0
    def Push(self,value):
        if len(self.stack)==0:
            self.stack.append(value)
            self.maximum=value
        elif value>self.maximum:
            self.stack.append(int(2*value)-int(self.maximum))
            self.maximum=value
        else:
            self.stack.append(value)
       
    def Pop(self):
        
        a=self.stack.pop()
        
        if int(a)>int(self.maximum):
            self.maximum=int(2*self.maximum)-a
          
    
    def Max(self):
        return self.maximum
        
   



n=int(input())
stack=findMaximum()
for i in range(n):
    queries=list(sys.stdin.readline().split())
    if queries[0]=="push":
        stack.Push(queries[1])
    elif queries[0]=="pop":
        stack.Pop()
    else:
        print(stack.Max())
