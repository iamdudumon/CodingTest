def binary(n):
    if n == 0:
        return ""
    
    return binary(n // 2) + str(n % 2)

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        bin = list(binary(arr1[i] | arr2[i]).rjust(n, '0'))
        temp = ""
        
        for ii in range(n - 1, -1, -1):
            if bin[ii] == '1':
                temp = '#' + temp
            else:
                temp = ' ' + temp
                
        answer.append(temp)
    
    return answer