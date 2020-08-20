from collections import deque


    
   




n=int(input())
numbers=[int(i) for i in input().split()]
window_size=int(input())
main_queue=deque()
track_queue=deque()

for i in numbers[0:window_size]:
    if len(main_queue)==0:
        main_queue.append(i)
        track_queue.append(i)
        
    
    elif i > track_queue[-1]:
        while track_queue and i>track_queue[-1]:
           track_queue.pop()
        track_queue.append(i) 
        main_queue.append(i)
    else:
        track_queue.append(i)
        main_queue.append(i)
print(track_queue[0],end=" ")
for i in numbers[window_size:n]:
    #print(i,"this is i")
    #print(track_queue,main_queue)
    if i > track_queue[-1]:
        while track_queue and i>track_queue[-1]:
           track_queue.pop()
        track_queue.append(i) 
        main_queue.append(i)
        #print(track_queue)
        if track_queue[0]==main_queue[0]:
           track_queue.popleft()
           main_queue.popleft()
        else:
           main_queue.popleft() 
        #print(track_queue,main_queue)   
        print(track_queue[0],end=" ")       
    else:
        track_queue.append(i)
        main_queue.append(i)
        if track_queue[0]==main_queue[0]:
           track_queue.popleft()
           main_queue.popleft()
        else:
           main_queue.popleft() 
        print(track_queue[0],end=" ")   
   
    #print(track_queue,main_queue)        
    #print(track_queue[0],end=" ")
    
