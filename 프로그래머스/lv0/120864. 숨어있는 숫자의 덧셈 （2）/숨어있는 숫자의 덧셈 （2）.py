def solution(my_string):
    answer = 0

    num_ch = "0"
    for i in range(len(my_string)):
        ch = my_string[i]
        try:
            int(ch)
            num_ch += ch
            
        except:
            answer += int(num_ch)
            num_ch = "0"
    
    answer += int(num_ch)

    return answer