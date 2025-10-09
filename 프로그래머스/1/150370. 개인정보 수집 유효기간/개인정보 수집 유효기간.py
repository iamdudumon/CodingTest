def minus_days(day1, day2):
    day1 = day1.split(".")
    day2 = day2.split(".")
    
    total_day1 = int(day1[0]) * (12 * 28) + int(day1[1]) * 28 + int(day1[2])
    total_day2 = int(day2[0]) * (12 * 28) + int(day2[1]) * 28 + int(day2[2].split(' ')[0])
                     
    return total_day1 - total_day2
                     
def solution(today, terms, privacies):
    answer = []
    
    term_dics = {}
    for term in terms:
        temp = term.split(" ")
        term_dics[temp[0]] = int(temp[1])
    # print(term_dics)
    for idx, pri in enumerate(privacies):
        # print(minus_days(today, pri), term_dics[pri[-1]] * 28)
        if minus_days(today, pri) >= term_dics[pri[-1]] * 28:
            answer.append(idx + 1)
        
    return answer