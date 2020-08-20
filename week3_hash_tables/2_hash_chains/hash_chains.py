# python3




class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [[] for i in range (self.bucket_count)]

    def _hash_func(self, s):
        ans = 0
        
        for c in reversed(s):
            #print(c,end=" ")
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def check(self,index):
        print(' '.join(self.elems[index]))
    def add(self,string):
        hashed=self._hash_func(string)
        if string not in self.elems[hashed]:
            self.elems[hashed]= [string]+self.elems[hashed]
    def delete(self,string):
        hashed=self._hash_func(string)
        if string in self.elems[hashed]:
            self.elems[hashed].remove(string)
            
    def find(self,string):
        hashed=self._hash_func(string)
        if string in self.elems[hashed]:
            print("yes")
        else:
            print("no")
    def process_queries(self):
        n = int(input())
        for i in range(n):
            query=list(input().split())
            if query[0]=="add":
                self.add(query[1])
            elif query[0]=="check":
                self.check(int(query[1]))
            elif query[0]=="find":
                self.find(query[1])
            else:
                self.delete(query[1])
if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
