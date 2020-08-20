import sys
import threading
sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class tree_traversal:
    def __init__(self):
        self.n=int(input())
        self.key=[None]*self.n
        self.left=[None]*self.n
        self.right=[None]*self.n
        for i in range(self.n):
            self.key[i],self.left[i],self.right[i]=map(int,input().split())
        
    def inOrderTraversal(self,root):
        if root!=-1:
            self.inOrderTraversal(self.left[root])
            print(self.key[root],end=" ")
            self.inOrderTraversal(self.right[root])
            
    def preOrderTraversal(self,root):
        if root!=-1:
           print(self.key[root],end=" ") 
           self.preOrderTraversal(self.left[root])
           self.preOrderTraversal(self.right[root])
    def postOrderTraversal(self,root) :
        if root!=-1:
            self.postOrderTraversal(self.left[root])
            self.postOrderTraversal(self.right[root])
            print(self.key[root],end=" ")
def main():    
    tree=tree_traversal()    
    tree.inOrderTraversal(0)
    print()
    tree.preOrderTraversal(0)
    print()
    tree.postOrderTraversal(0)

threading.Thread(target=main).start()
