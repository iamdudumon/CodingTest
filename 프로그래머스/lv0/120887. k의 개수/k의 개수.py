def solution(i, j, k):
    answer = 0
    k_str = str(k)

    for num in range(i, j+1):
        ch = str(num)

        if not k_str in ch:
            continue

        for c in ch:
            if c == k_str:
                answer += 1

    return answer
