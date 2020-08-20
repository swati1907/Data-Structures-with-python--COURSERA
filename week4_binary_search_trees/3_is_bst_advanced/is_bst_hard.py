#!/usr/bin/python3
import sys
import math
import threading
sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
class tree_traversal:
    def __init__(self):
        self.n=int(input())
        if self.n==0:
            print("CORRECT")
            sys.exit()
        self.key=[None]*self.n
        self.left=[None]*self.n
        self.right=[None]*self.n
        self.prev=-math.inf
        for i in range(self.n):
            self.key[i],self.left[i],self.right[i]=map(int,input().split())
        
    def isBinarySearchTree(self,root,minimum,maximum):
        if root!=-1:
            
             
            self.isBinarySearchTree(self.left[root],minimum,self.key[root])
            if self.key[root]>=maximum or self.key[root]<minimum :
                print("INCORRECT")
                sys.exit()
              
            self.isBinarySearchTree(self.right[root],self.key[root],maximum)
            return True
def main():    
    tree=tree_traversal() 
   
    if tree.isBinarySearchTree(0,-math.inf,math.inf):
        
        print("CORRECT")
   
threading.Thread(target=main).start()
