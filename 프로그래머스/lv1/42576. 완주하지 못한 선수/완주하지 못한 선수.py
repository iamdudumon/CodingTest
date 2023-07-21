def solution(participant, completion):
    answer = ''

    participant_dic = {}    #people:(1 if not people in participant_dic.keys() else participant_dic[people] + 1) for people in participant}
    for people in participant:
        if people in participant_dic.keys():
            participant_dic[people] += 1
        else:
            participant_dic[people] = 1

    for people in completion:
        if participant_dic[people] == 1:
            del participant_dic[people]
        else:
            participant_dic[people] += -1
            
    for people in participant_dic.keys():
        answer = people

    return answer

print(solution(["leo", "kiki", "eden"],	["eden", "kiki"]))