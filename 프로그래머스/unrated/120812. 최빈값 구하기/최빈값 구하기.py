def solution(array):
    answer = 0
    count = {}
    
    for item in array:
        count[item] = count.get(item, 0) + 1
        
    max_pair= [0, 0]
    duplicate_state = False
    for key, value in count.items():
        if value > max_pair[1]:
            max_pair[0] = key
            max_pair[1] = value
            duplicate_state = False
        elif value == max_pair[1]:
            duplicate_state = True
    
    return -1 if duplicate_state else max_pair[0]