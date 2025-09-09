import sys
import heapq

input = sys.stdin.readline

T = 0
while True:
    N = int(input())
    if N == 0:
        break
    
    matrix = [list(map(int, input().split())) for _ in range(N)]
    dp = [[10**15] * N for _ in range(N)]
    dp[0][0] = matrix[0][0]
    heap = []
    heapq.heappush(heap, (dp[0][0], 0, 0))

    while heap:
        cost, r, c = heapq.heappop(heap)

        if cost > dp[r][c]:
            continue
        if (r, c) == (N-1, N-1):
            break

        for m in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + m[0], c + m[1]
            if 0 <= nr < N and 0 <= nc < N:
                new_cost = cost + matrix[nr][nc]
                if dp[nr][nc] > new_cost:
                    dp[nr][nc] = new_cost
                    heapq.heappush(heap, (new_cost, nr, nc))

    print(f"Problem {T+1}:", dp[-1][-1])
    
    T+=1