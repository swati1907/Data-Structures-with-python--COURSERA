# python3
from collections import deque
import sys, threading
#sys.setrecursionlimit(10**7) # max depth of recursion
#threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
    def __init__(self,value):
        self.value=value
        self.children=deque()

class TreeHeight:
        def read(self):
                
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
                
        def compute_height(self):
                nodes=[Node(i) for i in range(self.n)]
                for i in range(self.n):
                    if self.parent[i]==-1:
                        self.root=nodes[i]
                    else:
                        nodes[self.parent[i]].children.append(nodes[i])
                height=0 
                q=deque()
                q.append(self.root)
                while len(q)!=0 :
                    
                    height+=1
                    #print(height,"height")    
                    for i in range(len(q)):
                        
                        
                        b=q.popleft()
                        q+=b.children
                        
                return height;
tree = TreeHeight()
tree.read()
print(tree.compute_height())

  #threading.Thread(target=main).start()
