def solution(arr1, arr2):
    answer = []

    for idx in range(len(arr1)):
        temp = []
        for i in range(len(arr1[idx])):
            temp.append(arr1[idx][i] + arr2[idx][i])
        answer.append(temp)

    return answer
