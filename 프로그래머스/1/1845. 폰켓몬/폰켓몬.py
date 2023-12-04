def solution(nums):
    answer = 0
    poketmon_set = set(nums)
    
    size = len(nums)//2
    
    return size if len(poketmon_set) >= size else len(poketmon_set)