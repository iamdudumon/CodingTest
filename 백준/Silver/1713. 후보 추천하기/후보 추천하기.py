import heapq

n = int(input())
s_num = int(input())

candidate_list = list(map(int, input().split()))

candidate_dic = {}
level_list = []
min_level = 0


for _ in range(s_num):
    level_list.append([])

for idx in range(s_num):
    candidate = candidate_list[idx]
    
    if not candidate_dic.__contains__(candidate):
        if len(candidate_dic) == n:
            while True:
                deleted_candidate = heapq.heappop(level_list[min_level])[1]
                if candidate_dic[deleted_candidate][1] == min_level:
                    del candidate_dic[deleted_candidate]
                    break
            
        candidate_dic[candidate] = [idx, 0]
        heapq.heappush(level_list[0], (idx, candidate))
        #level_list[0].put((idx, candidate))

        min_level = 0
    else:
        pre_idx, level = candidate_dic[candidate]
        candidate_dic[candidate][1] += 1
        heapq.heappush(level_list[level + 1], (pre_idx, candidate))
        #level_list[level + 1].put((idx, candidate))
        
        while len(level_list[min_level]) > 0:
            temp = level_list[min_level][0][1]
            if candidate_dic[temp][1] != min_level:
                heapq.heappop(level_list[min_level])
            else:
                break
          
        if len(level_list[min_level]) == 0:
            min_level = level + 1

answer = sorted([key for key in candidate_dic])
for idx in range(len(answer)):
    print(answer[idx], end=" ")
