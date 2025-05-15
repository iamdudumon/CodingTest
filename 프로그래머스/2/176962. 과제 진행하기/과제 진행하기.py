import heapq
from collections import deque

def convert_inttime(time):
    t = time.split(":")
    if len(t) < 2:
        return int(t[0])
    return int(t[0]) * 60 + int(t[1])

def solution(plans):
    answer = []
    deq = deque()
    
    for plan in plans:
        plan[1] = convert_inttime(plan[1])
        plan[2] = convert_inttime(plan[2])
    
    plans.sort(key=lambda x:x[1])
    print(plans)
    i = 0
    while True:
        if i < len(plans) - 1:
            work1 = plans[i]
            work2 = plans[i + 1]
            rest_time = work2[1] - (work1[1] + work1[2])
            
            if rest_time >= 0:   # 기존 work가 다 끝난 경우
                answer.append(work1[0])
                
                if deq:
                    while rest_time and deq:
                        work = deq.pop()
                        if work[2] > rest_time:
                            work[2] -= rest_time
                            deq.append(work)
                            rest_time = 0
                        else:
                            rest_time -= work[2]
                            answer.append(work[0])
            
            else:           # 기존 work가 끝나기 전 다음 work가 도착
                work1[2] -= (work2[1] - work1[1])
                deq.append(work1)
            
            i+=1
        else:
            work = plans[i]
            answer.append(work[0])
            while deq:
                answer.append(deq.pop()[0])
            break
            
    return answer