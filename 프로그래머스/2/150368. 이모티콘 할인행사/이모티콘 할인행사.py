def discount(money, dis):
    return ((100 - dis) / 100) * money

def solution(users, emoticons):
    answer = [0, 0]
    combis = [10] * len(emoticons)
    end_flag = len(emoticons) * 40
    
    while True:
        plus = cost = 0
        price = [discount(emoticons[i], combis[i]) for i in range(len(emoticons))]
        
        for user in users:
            user_total = 0
            for idx, dis in enumerate(combis):
                if user[0] > dis:
                    continue
                user_total += price[idx]
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
        
        if sum(combis) == end_flag:
            break
    
        i = 0
        while i < len(emoticons):
            combis[i] += 10
            if combis[i] == 50:
                combis[i] = 10
                i += 1
            else:
                break
        
    
    return answer