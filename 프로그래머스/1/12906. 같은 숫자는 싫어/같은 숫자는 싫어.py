def solution(arr):
    answer = []
    
    start = -1
    for item in arr:
        if start != item:
            answer.append(item)
        start = item
    
    return answer