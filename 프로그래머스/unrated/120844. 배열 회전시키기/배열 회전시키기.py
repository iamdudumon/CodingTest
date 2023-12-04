from collections import deque

def solution(numbers, direction):
    answer = []
    deq = deque(numbers)
    if direction == "right":
        deq.rotate(1)
    else:
        deq.rotate(-1)
    return list(deq)