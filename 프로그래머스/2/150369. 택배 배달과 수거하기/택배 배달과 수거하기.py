import heapq

def solution(cap, n, deliveries, pickups):
    answer = 0
    del_sum = sum(deliveries)
    del_i, pic_i = n - 1, n - 1
    while del_i >= 0 and not deliveries[del_i]:
        del_i-=1
    while pic_i >= 0 and not pickups[pic_i]:
        pic_i-=1

    while del_i != -1 or pic_i != -1:
        jim = min(cap, del_sum)
        top = max(del_i, pic_i)
        while del_i != -1:
            if deliveries[del_i] > jim:
                deliveries[del_i]-=jim
                del_sum-=jim
                jim = 0
                break
            else:
                jim-=deliveries[del_i]
                del_sum-=deliveries[del_i]
                deliveries[del_i] = 0
                del_i-=1
        
        while pic_i != -1:
            if pickups[pic_i] > (cap - jim):
                pickups[pic_i]-=(cap - jim)
                jim = cap
                break
            else:
                jim+=pickups[pic_i]
                pickups[pic_i] = 0
                pic_i-=1
                
        answer+=(2 * (top + 1))
    
    return answer


