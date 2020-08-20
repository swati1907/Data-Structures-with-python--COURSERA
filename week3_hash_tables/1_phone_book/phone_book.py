class Query:
    def __init__(self, queries):
        self.queries=queries
        self.phonebook={}
    def process_queries (self):
        for query in self.queries:
            task=query[0]
            
            if task=='add':
                self.add(query[1],query[2])
            elif task=='find':
                self.find(query[1])
                
            else:
                self.delete(query[1])
                
                
    def add(self,number,name):
        self.phonebook[number]=name
    
    def find(self,number):
        if number in self.phonebook:
            print(self.phonebook[number])
        else:
            print("not found")
    def delete(self,number):
        if number in self.phonebook:
                    
            del self.phonebook[number]
        
      
n = int(input())


queries=[list(input().split()) for i in range(n)]
qp=Query(queries)
qp.process_queries()
