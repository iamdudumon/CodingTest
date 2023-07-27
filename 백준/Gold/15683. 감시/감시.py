import sys
import copy

def move_area(matrix, direction, position):
    matrix = copy.deepcopy(matrix)

    cover_area = 0
    position[0] += direction[0]
    position[1] += direction[1]

    while position[0] < n and position[0] >= 0 and position[1] < m and position[1] >= 0 and matrix[position[0]][position[1]] != 6:
        if matrix[position[0]][position[1]] == 0:
            matrix[position[0]][position[1]] = -1
            cover_area += 1
        position[0] += direction[0]
        position[1] += direction[1]

    return matrix, cover_area

def observe_with_cctv(matrix, cctv_idx, cover_area=0):
    if cctv_idx == len(cctv_list):
        global max_cover
        if max_cover < cover_area:
            max_cover = cover_area
        return

    cctv, row, col = cctv_list[cctv_idx]

    if cctv == 1:
        for idx in range(4):
            cover_area_copy = cover_area
            direction = vertical_move[idx] if idx < 2 else horizontal_move[idx - 2]

            result = move_area(matrix, direction, [row, col])
            observe_with_cctv(result[0], cctv_idx + 1, cover_area_copy + result[1])
    elif cctv == 2:
        for idx in range(2):
            cover_area_copy = cover_area
            direction_1 = vertical_move[idx] if idx < 1 else horizontal_move[idx - 1]
            direction_2 = vertical_move[idx + 1] if idx < 1 else horizontal_move[idx]
    
            result = move_area(matrix, direction_1, [row, col])
            cover_area_copy += result[1]
            result = move_area(result[0], direction_2, [row, col])

            observe_with_cctv(result[0], cctv_idx + 1, cover_area_copy + result[1])
    elif cctv == 3:
        for idx in range(4):
            cover_area_copy = cover_area
            direction_1 = vertical_move[idx // 2] 
            direction_2 = horizontal_move[idx % 2]

            result = move_area(matrix, direction_1, [row, col])
            cover_area_copy += result[1]
            result = move_area(result[0], direction_2, [row, col])

            observe_with_cctv(result[0], cctv_idx + 1, cover_area_copy + result[1])
    elif cctv == 4:
        temp_move = vertical_move + horizontal_move
        for idx in range(4):
            cover_area_copy = cover_area
            direction_1 = temp_move[idx%4] 
            direction_2 = temp_move[(idx+1)%4]
            direction_3 = temp_move[(idx+2)%4]

            result = move_area(matrix, direction_1, [row, col])
            cover_area_copy += result[1]
            result = move_area(result[0], direction_2, [row, col])
            cover_area_copy += result[1]
            result = move_area(result[0], direction_3, [row, col])

            observe_with_cctv(result[0], cctv_idx + 1, cover_area_copy + result[1])
    else:
        cover_area_copy = cover_area
        direction_1 = vertical_move[0] 
        direction_2 = vertical_move[1]
        direction_3 = horizontal_move[0]
        direction_4 = horizontal_move[1]
        
        result = move_area(matrix, direction_1, [row, col])
        cover_area_copy += result[1]
        result = move_area(result[0], direction_2, [row, col])
        cover_area_copy += result[1]
        result = move_area(result[0], direction_3, [row, col])
        cover_area_copy += result[1]
        result = move_area(result[0], direction_4, [row, col])

        observe_with_cctv(result[0], cctv_idx + 1, cover_area_copy + result[1])
    
n, m = map(int, sys.stdin.readline().split())

matrix = []
cctv_list = []
wall_list = []
vertical_move = [(1,0),  (-1, 0)]
horizontal_move = [(0,1), (0, -1)]
max_cover = 0

for i in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        if line[j] == 6:
            wall_list.append((i, j))
        elif line[j] > 0:
            cctv_list.append((line[j], i, j))
    matrix.append(line)

observe_with_cctv(matrix, 0)
print(n*m - len(cctv_list) - len(wall_list) - max_cover)