import sys
import copy

def move_area(matrix, cover_area, direction, position):
    position[0] += direction[0]
    position[1] += direction[1]

    while position[0] < n and position[0] >= 0 and position[1] < m and position[1] >= 0 and matrix[position[0]][position[1]] != 6:
        if matrix[position[0]][position[1]] == 0:
            matrix[position[0]][position[1]] = -1
            cover_area += 1
        position[0] += direction[0]
        position[1] += direction[1]

    return cover_area

def observe_with_cctv(matrix, cctv_idx, cover_area=0):
    if cctv_idx == len(cctv_list):
        global max_cover
        max_cover = max(max_cover, cover_area)
        return

    cctv, row, col = cctv_list[cctv_idx]\
    
    if cctv == 1:
        for idx in range(4):
            matrix_copy = copy.deepcopy(matrix)
            cover_area_copy = cover_area
            
            direction = vertical_move[idx] if idx < 2 else horizontal_move[idx - 2]

            cover_area_copy = move_area(matrix_copy, cover_area_copy, direction, [row, col])
            observe_with_cctv(matrix_copy, cctv_idx + 1, cover_area_copy)
    elif cctv == 2:
        for idx in range(2):
            matrix_copy = copy.deepcopy(matrix)
            cover_area_copy = cover_area
            
            direction_1 = vertical_move[idx] if idx < 1 else horizontal_move[idx - 1]
            direction_2 = vertical_move[idx + 1] if idx < 1 else horizontal_move[idx]
            
            cover_area_copy = move_area(matrix_copy, cover_area_copy, direction_1, [row, col])
            cover_area_copy = move_area(matrix_copy, cover_area_copy, direction_2, [row, col])

            observe_with_cctv(matrix_copy, cctv_idx + 1, cover_area_copy)
    elif cctv == 3:
        for idx in range(4):
            matrix_copy = copy.deepcopy(matrix)
            cover_area_copy = cover_area
            
            direction_1 = vertical_move[idx // 2] 
            direction_2 = horizontal_move[idx % 2]

            cover_area_copy = move_area(matrix_copy, cover_area_copy, direction_1, [row, col])
            cover_area_copy = move_area(matrix_copy, cover_area_copy, direction_2, [row, col])

            observe_with_cctv(matrix_copy, cctv_idx + 1, cover_area_copy)
    elif cctv == 4:
        for idx in range(4):
            matrix_copy = copy.deepcopy(matrix)
            cover_area_copy = cover_area
            
            direction_1 = temp_move[idx%4] 
            direction_2 = temp_move[(idx+1)%4]
            direction_3 = temp_move[(idx+2)%4]

            cover_area_copy = move_area(matrix_copy, cover_area_copy, direction_1, [row, col])
            cover_area_copy = move_area(matrix_copy, cover_area_copy, direction_2, [row, col])
            cover_area_copy = move_area(matrix_copy, cover_area_copy, direction_3, [row, col])

            observe_with_cctv(matrix_copy, cctv_idx + 1, cover_area_copy)
    else:
        matrix_copy = copy.deepcopy(matrix)
        cover_area_copy = cover_area
        
        direction_1 = vertical_move[0] 
        direction_2 = vertical_move[1]
        direction_3 = horizontal_move[0]
        direction_4 = horizontal_move[1]
        
        cover_area_copy = move_area(matrix_copy, cover_area_copy, direction_1, [row, col])
        cover_area_copy = move_area(matrix_copy, cover_area_copy, direction_2, [row, col])
        cover_area_copy = move_area(matrix_copy, cover_area_copy, direction_3, [row, col])
        cover_area_copy = move_area(matrix_copy, cover_area_copy, direction_4, [row, col])

        observe_with_cctv(matrix_copy, cctv_idx + 1, cover_area_copy)
    
n, m = map(int, sys.stdin.readline().split())
matrix = []
cctv_list = []
wall_count = 0
vertical_move = [(1,0),  (-1, 0)]
horizontal_move = [(0,1), (0, -1)]
temp_move = vertical_move + horizontal_move
max_cover = 0

for i in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        if line[j] == 6:
            wall_count += 1
        elif line[j] > 0:
            cctv_list.append((line[j], i, j))
    matrix.append(line)

observe_with_cctv(matrix, 0)
print(n*m - len(cctv_list) - wall_count - max_cover)