from collections import deque

def solution(s):
    answer = 0
    
    deq = deque()
    s = s.split(" ")
    
    for i in s:
        if i == "Z":
            deq.pop()
        else:
            deq.append(int(i))
    
    for i in deq:
        answer += i
    
    return answer