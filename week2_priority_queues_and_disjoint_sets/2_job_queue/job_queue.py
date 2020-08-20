# python3
import heapq
from collections import namedtuple
AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

class Workers_database:
    def __init__(self,thread,release_time=0):
        self.thread=thread
        self.release_time=release_time
        
    def __lt__(self,other):
        if self.release_time==other.release_time:
            return self.thread<other.thread
        return self.release_time<other.release_time
    
    def __gt__(self,other):
        if self.release_time==other.release_time:
            return self.thread>other.thread
        return self.release_time>other.release_time
class job_queue:
    def __init__(self,n_workers):
        self.jobs=list(map(int, input().split()))
        self.n_workers=n_workers
        self.workers=[Workers_database(i) for i in range(n_workers)]
   
    def solve(self):
        for i in self.jobs:
            a_worker=heapq.heappop(self.workers)#returns element with least priority
            m=AssignedJob(a_worker.thread,a_worker.release_time)
            a_worker.release_time+=i
            b=heapq.heappush(self.workers,a_worker)
            print(m.worker,m.started_at)
            
            

def main():
    n_workers, n_jobs = map(int, input().split())
    
    assigned_jobs=job_queue(n_workers)
    assigned_jobs.solve()

    
if __name__ == "__main__":
    main()
