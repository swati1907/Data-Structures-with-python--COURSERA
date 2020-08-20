# python3
import sys
class buildHeap:
    def __init__(self,n):
        self.swap=0
        self.n=n
        self.a=list(map(int,sys.stdin.read().split()))
        self.num=[]
        self.countSwaps()
    
    def sift_down(self,i):
        m=i
        left=(2*i)+1
        right=(2*i)+2
        if left<n and self.a[left]<self.a[i]:
            m=left
        if right<n and self.a[right]<self.a[m]:
            m=right
    
        if(i!=m):
            self.a[i],self.a[m]=self.a[m],self.a[i]
            self.num.append(i)
            self.num.append(m)
            self.swap+=1
            self.sift_down(m)
    def countSwaps(self):
        for i in range((self.n)//2,-1,-1):
            self.sift_down(i)
        print(self.swap)    
        for i in range(0,len(self.num)-1,2): 
            print(self.num[i],self.num[i+1])

        
n=int(input())
heap=buildHeap(n)

   
