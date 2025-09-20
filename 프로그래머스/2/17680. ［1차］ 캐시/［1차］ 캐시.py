from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    if cacheSize == 0:
        return len(cities) * 5
    
    que = deque()
    cache = set()
    
    for ccity in cities:
        city = ccity.lower()
        if city in cache:
            answer+=1
            que.remove(city)
            que.append(city)
        else:
            answer+=5
            que.append(city)
            cache.add(city)
            if len(que) > cacheSize:
                cache.remove(que.popleft())
    
    return answer