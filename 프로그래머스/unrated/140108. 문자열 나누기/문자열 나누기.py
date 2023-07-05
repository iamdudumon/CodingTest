def solution(s):
    answer = 0

    j = 0
    while j < len(s):
        x = s[j]
        count_x = 1
        count_others = 0
        for i in range(j + 1, len(s)):
            if s[i] == x:
                count_x += 1
            else:
                count_others +=1
            
            # i == len(s) - 1 -> 더 이상 읽을 문자가 없다면 종료
            if i == len(s) - 1:
                return answer + 1
            
            if count_x == count_others:
                answer += 1
                j = i + 1
                break;
    
        # 분리하고 남은 문자의 사이즈가 1인 경우 -> 다음 문자가 없으므로 for 문이 안 돌아가서 while 문을 탈출 못 함!
        if j == len(s) - 1:
            return answer + 1

    return answer
