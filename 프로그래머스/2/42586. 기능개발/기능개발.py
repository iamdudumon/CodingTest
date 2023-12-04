from collections import deque

def solution(progresses, speeds):
    answer = []
    deq = deque(progresses)
    pop = 0
    
    while deq:
        for idx in range(len(deq)):
            deq[idx]+=speeds[idx+pop]
        
        count = 0
        while deq and deq[0] >= 100:
            deq.popleft()
            count+=1
            pop+=1
            
        if count != 0:
            answer.append(count)
            
    return answer