def dfs(n, computers, visited):
    visited[n] = 1
    for i in range(len(computers[n])):
        if i == n or visited[i]:
            continue
        if computers[n][i]:
            visited[i] = 1
            dfs(i, computers, visited)

def solution(n, computers):
    answer = 0
    
    visited = [0] * n
    
    for i in range(len(computers)):
        if not visited[i]:
            dfs(i, computers, visited)
            answer+=1
    # print(visited)
    return answer