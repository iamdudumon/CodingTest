def minus_days(today, date):
    year, mon, day = map(int, date.split("."))                  
    return today - (year * (12 * 28) + mon * 28 + day)

def solution(today, terms, privacies):
    answer = []
    todays = today.split(".")
    today_num = int(todays[0]) * (12 * 28) + int(todays[1]) * 28 + int(todays[2])
    term_dics = {}
    for term in terms:
        temp = term.split(" ")
        term_dics[temp[0]] = int(temp[1])

    for idx, pri in enumerate(privacies):
        if minus_days(today_num, pri[:-1]) >= term_dics[pri[-1]] * 28:
            answer.append(idx + 1)
        
    return answer