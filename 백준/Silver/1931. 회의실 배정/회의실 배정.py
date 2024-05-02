import sys

input = sys.stdin.readline

def fill_room_time(start, end):
    if len(time) == 0:
        time.append((start, end))
        return True
    if  start < time[-1][1]:
        return
    time.append((start, end))

n = int(input())
room_list = [tuple(map(int, input().split())) for _ in range(n)]
room_list.sort(key=lambda x: (x[1], x[0]))
time = []

for room in room_list:
    fill_room_time(room[0], room[1])

print(len(time))