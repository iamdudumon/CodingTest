def solution(my_string):
    my_string = my_string.split(" ")

    sum = int(my_string[0])
    for i in range(1, len(my_string)):
        if my_string[i] == "+" or my_string[i] == "-":
            op = my_string[i]
            continue
        elif i != 0:
            sum = sum + int(my_string[i]) if op == "+" else sum - int(my_string[i])
        
    return sum