# python3


class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(self.row_counts)
        n_tables = len(row_counts)
        self.ranks = [0] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, a,b):
        b_id = self.get_parent(b)
        a_id = self.get_parent(a)
        #print(a_id,b_id,"roots")

        if b_id == a_id:
            return 
        if self.ranks[b_id]>self.ranks[a_id]:
            self.parents[a_id]=b_id
            self.row_counts[b_id]+=self.row_counts[a_id]
        else:
            self.parents[b_id]=a_id
            if self.ranks[b_id]==self.ranks[a_id]:
                
                self.ranks[a_id]+=1
            self.row_counts[a_id]+=self.row_counts[b_id]
            #self.row_counts[b_id]+=self.row_counts[a_id]
            
        #print(self.row_counts,self.parents,self.ranks,"counts,parents")
        self.max_row_count=max(self.max_row_count,self.row_counts[a_id],self.row_counts[b_id])
        return
        # merge two components
        # use union by rank heuristic
        # update max_row_count with the new maximum i size
        

    def get_parent(self, i):
        if i!=self.parents[i]:
            self.parents[i]=self.get_parent(self.parents[i])
        #print(self.parents)    
            
        return self.parents[i]


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    
    db = Database(counts)
    for i in range(n_queries):
        a, b = map(int, input().split())
        db.merge(a - 1, b - 1)
        print(db.max_row_count)


if __name__ == "__main__":
    main()
