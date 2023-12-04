from collections import deque

def solution(s):
    deq = deque()
    
    count = 0
    for ch in s:
        deq.append(ch)
        if ch == ")":
            if count > 0:
                deq.pop()
                deq.pop()
                count += -1
        else:
            count += 1
    
    print(deq)
    return len(deq) ==  0