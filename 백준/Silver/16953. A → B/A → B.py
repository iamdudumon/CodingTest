from collections import deque

def ab_bfs(start, final):
    queue = deque()
    queue.append((start, 1))

    flag = False
    while queue:
        item = queue.popleft()
        if item[0] > final:
            continue

        result1 = item[0] * 2
        result2 = item[0] * 10 + 1
        count = item[1] + 1

        if result1 == final or result2 == final:
            flag = True
            break
        else:
            if result1 not in visitied:
                queue.append((result1, count))
                visitied.add(result1)
            if result2 not in visitied:   
                queue.append((result2, count))
                visitied.add(result2)
    
    return count if flag else -1

a, b = map(int, input().split())
visitied = set()

answer = ab_bfs(a,b)
print(answer)