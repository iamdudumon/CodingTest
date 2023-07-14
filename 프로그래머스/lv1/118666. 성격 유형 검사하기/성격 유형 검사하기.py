def solution(survey, choices):
    answer = ''

    kakao_dic = {}
    kakao_dic["R"] = 0
    kakao_dic["T"] = 0
    kakao_dic["C"] = 0
    kakao_dic["F"] = 0
    kakao_dic["J"] = 0
    kakao_dic["M"] = 0
    kakao_dic["A"] = 0
    kakao_dic["N"] = 0

    for idx in range(len(survey)):
        if choices[idx] >= 4:
            kakao_dic[survey[idx][1]] += choices[idx] - 4
        else:
            kakao_dic[survey[idx][0]] += 4 - choices[idx]

    for key in kakao_dic:
        print(key + ", " + str(kakao_dic[key]))

    answer += 'R' if kakao_dic["R"] >= kakao_dic["T"] else 'T'
    answer += 'C' if kakao_dic["C"] >= kakao_dic["F"] else 'F'
    answer += 'J' if kakao_dic["J"] >= kakao_dic["M"] else 'M'
    answer += 'A' if kakao_dic["A"] >= kakao_dic["N"] else 'N'

    return answer