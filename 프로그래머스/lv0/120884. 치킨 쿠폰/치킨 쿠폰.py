def solution(chicken):
    answer = -1
    real_chicken = 0

    while chicken >= 10:
        real_chicken += chicken // 10
        chicken = chicken % 10 + chicken // 10


    return real_chicken