def solution(targets):
    answer = 0
    
    targets.sort(key=lambda x: x[1])
    
    e = targets[0][1]
    answer+=1
    
    for p in targets:
        if e > p[0]:
            continue
        else:
            answer+=1
            e = p[1]
    
    
#     p_min = min(targets, key=lambda x : x[0])[0]
#     p_max = max(targets, key=lambda x : x[1])[1]
#     cnt = 0
#     len_targets = len(targets)
#     missiles = [[p_max + 1, -1, set()] for _ in range(p_max + 1)]# * (p_max + 1)# * 2
#     del_missiles = [0] * len_targets
    
#     while cnt < len_targets:
#         for idx, point in enumerate(targets):
#             if del_missiles[idx]:
#                 continue
#             x1, x2 = point
#             for i in range(x1, x2):
#                 missiles[i][0] = min(missiles[i][0], x1)
#                 missiles[i][1] = max(missiles[i][1], x2)
#                 missiles[i][2].add((x1, x2, idx))
        
#         max_mis = max(missiles, key=lambda x: x[1] - x[0])
#         # print(max_mis)
#         for tt in max_mis[2]:
#             # print(tt)
#             del_missiles[tt[2]] = 1
#             cnt += 1
#         answer += 1
    # print(missiles)
    return answer