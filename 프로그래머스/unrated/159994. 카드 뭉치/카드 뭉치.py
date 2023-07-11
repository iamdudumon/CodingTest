def solution(cards1, cards2, goal):
    i = 0
    j = 0
    k = 0

    while k < len(goal):
        if i < len(cards1) and cards1[i] == goal[k]:
            i += 1
            k += 1
        elif j < len(cards2) and cards2[j] == goal[k]:
            j += 1
            k += 1
        else:
            return "No"       

    return "Yes"
