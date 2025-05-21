import copy

def solution(land):
    answer = 0

    dp = [0] * 4
    dp[0] = land[0][0]
    dp[1] = land[0][1]
    dp[2] = land[0][2]
    dp[3] = land[0][3]
    for i in range(1, len(land)):
        temp = copy.deepcopy(dp)
        dp[0] = max(temp[1], temp[2], temp[3]) + land[i][0]
        dp[1] = max(temp[0], temp[2], temp[3]) + land[i][1]
        dp[2] = max(temp[0], temp[1], temp[3]) + land[i][2]
        dp[3] = max(temp[0], temp[1], temp[2]) + land[i][3]

    answer = max(dp)
    return answer