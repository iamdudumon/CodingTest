def discount(money, dis):
    # return int(((100 - dis) / 100) * money)
    return (1 - dis*0.01)*100*money/100;

def solution(users, emoticons):
    answer = [0, 0]
    combi = [10] * len(emoticons)
    
    while True:
        plus = cost = 0

        for user in users:
            user_total = 0
            for idx, co in enumerate(combi):
                if user[0] > co:
                    continue
                user_total += discount(emoticons[idx], co)
                if user_total >= user[1]:
                    break
            if user_total >= user[1]:
                plus += 1
            else:
                cost += user_total
        
        if answer[0] < plus:
            answer[0] = plus
            answer[1] = cost
        elif answer[0] == plus:
            answer[1] = max(answer[1], cost)
            
        
        if sum(combi) == len(emoticons) * 40:
            break
        
        i = 0
        while i < len(emoticons):
            combi[i] += 10
            if combi[i] == 50:
                combi[i] = 10
                i += 1
            else:
                break
        
    
    return answer