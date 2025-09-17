def binary(n):
    if n == 0:
        return ""
    
    return binary(n // 2) + str(n % 2)

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        bin = list(binary(arr1[i] | arr2[i]))
        temp = ""
        
        j = len(bin) - 1
        for ii in range(n - 1, -1, -1):
            if bin[j] == '1' and j >= 0:
                temp = '#' + temp
            else:
                temp = ' ' + temp
            j-=1
                
        answer.append(temp)
    
    return answer