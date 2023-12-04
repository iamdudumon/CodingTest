from string import ascii_lowercase
 
def solution(s, skip, index):
    answer = ''
    alpha_list = list(ascii_lowercase)
    skip = set(list(skip))
    alpha_list = [alpha for alpha in alpha_list if not alpha in skip]
    alpha_dic = {alpha: idx for idx, alpha in enumerate(alpha_list)}
    
    print(alpha_dic)
    
    for ch in s:
        answer += alpha_list[(alpha_dic[ch] + index ) % len(alpha_list)]
        
    return answer