import sys
import math

def distance(x0, y0, x1, y1):
    return math.sqrt((x0-x1)**2 + (y0-y1)**2)

n = int(sys.stdin.readline())

for _ in range(n):
    x0, y0, x1, y1 = map(int, sys.stdin.readline().split())
    distance_xy = distance(x0, y0, x1, y1)

    answer = 0
    planet_num = int(sys.stdin.readline())

    for _ in range(planet_num):
        x, y, d = map(int, sys.stdin.readline().split())
        starting_poing_distance = distance(x0, y0, x, y)
        destination_distance = distance(x1, y1, x, y)

        if starting_poing_distance < d and destination_distance > d:  # 출발지는 어떤 행성 반경 안에 존재하나 도착지는 행성 밖에 존재
            answer += 1
        elif starting_poing_distance > d and destination_distance < d: # 반대로 출발지는 행성 밖에 존재, 도착지는 행성 안에 존재
            answer += 1

    print(answer)