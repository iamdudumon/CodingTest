def solution(clothes):
    answer = 1

    clothes_dic = {}\

    for clothe in clothes:
        if clothes_dic.__contains__(clothe[1]):
            clothes_dic[clothe[1]] += 1
        else:
            clothes_dic[clothe[1]] = 1

    for clothe in clothes_dic:
        answer *= clothes_dic[clothe] + 1

    return answer - 1