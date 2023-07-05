def solution(my_string, num1, num2):
    answer = ''
    temp_str = my_string[num1]

    for i in range(len(my_string)):
        ch = my_string[i]
        if  i == num1:
            answer += my_string[num2]
        elif i == num2:
            answer += temp_str
        else:
            answer += ch

    return answer