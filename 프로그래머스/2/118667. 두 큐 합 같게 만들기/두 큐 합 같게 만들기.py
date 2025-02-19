from collections import deque

def solution(queue1, queue2):
    q1_sum, q2_sum = sum(queue1), sum(queue2)
    q1, q2 = deque(queue1), deque(queue2)
    q_len = 2 * len(queue1)
    
    if q1_sum == q2_sum:
        return 0
    if (q1_sum + q2_sum) % 2 != 0:
        return -1
    
    answer = 0
    while answer < 2 * q_len:
        if q1_sum < q2_sum:
            num = q2.popleft()
            q1.append(num)
            q1_sum += num
            q2_sum -= num
            answer += 1
        elif q1_sum > q2_sum:
            num = q1.popleft()
            q2.append(num)
            q1_sum -= num
            q2_sum += num
            answer += 1
        else :
            return answer
    
    
    return -1