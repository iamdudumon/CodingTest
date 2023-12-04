from collections import deque

def solution(priorities, location):
    answer = 0
    deq = deque(priorities)
    priority_sorted_que = deque(sorted(priorities, reverse=True))
    
    while True:
        p = deq.popleft()
        if p == priority_sorted_que[0]:
            answer+=1
            priority_sorted_que.popleft()
            if location == 0:
                break
        else:
            deq.append(p)       
        location = (location-1)%len(deq)
    
    return answer