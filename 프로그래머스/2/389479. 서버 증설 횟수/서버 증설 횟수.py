def solution(players, m, k):
    answer = 0
    
    servers = [0] * 24
    current = 0
    
    for i, p in enumerate(players):
        current -= servers[i - k] if i >= k else 0

        if (current + 1) * m > p:
            continue
        servers[i] = (p - (current + 1) * m) // m  + 1
        current += servers[i]
        answer += servers[i]

    return answer