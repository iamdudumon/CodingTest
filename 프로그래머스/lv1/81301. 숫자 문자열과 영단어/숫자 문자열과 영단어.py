def solution(s):
    answer = 0
    
    number_dic = {}
    number_dic["zero"] = 0
    number_dic["one"] = 1
    number_dic["two"] = 2
    number_dic["three"] = 3
    number_dic["four"] = 4
    number_dic["five"] = 5
    number_dic["six"] = 6
    number_dic["seven"] = 7
    number_dic["eight"] = 8
    number_dic["nine"] = 9

    number_list= ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    i = 0

    while True:
        try:
            s = int(s)
            answer = s
            break
        except:
            if number_list[i] in s:
                s = s.replace(number_list[i], str(number_dic[number_list[i]]))
            
        i += 1
        if i % 10 == 0:
            i = 0

    print(type(answer))
    return answer

print(solution("one4seveneight"))