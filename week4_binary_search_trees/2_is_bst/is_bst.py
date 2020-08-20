#!/usr/bin/python3
import sys
import math
import threading
sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
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
        #print(self.key,self.left,self.right)
            
    def isBinarySearchTree(self,root):
        if root!=-1:
            self.isBinarySearchTree(self.left[root])
            #print(self.prev,self.key[root])
            if self.prev>self.key[root]:
                print("INCORRECT")
                sys.exit()
            self.prev=self.key[root]
            self.isBinarySearchTree(self.right[root])
        return True

def main():    
    tree=tree_traversal() 
    #print("11111111111")
    if tree.isBinarySearchTree(0):
        print("CORRECT")
   
threading.Thread(target=main).start()
