def sum_tuple(tuple):
    sum = 0
    for item in tuple:
        sum += item[0]

    return sum

def solution(genres, plays):
    answer = []

    best = {}
    for idx, item in enumerate(genres):
        if item not in best:
            best[item] = []
            best[item].append((plays[idx], idx))
        else:
            best[item].append((plays[idx], idx))

    
    while len(best) > 0:
        max_sum = 0 
        for key, value in best.items():
            temp_sum = sum_tuple(value)
            if max_sum < temp_sum:
                max_sum = temp_sum
                max_album = best[key]
                max_key = key
        
        for idx in range(2 if len(max_album) >= 2 else 1):
            max_song = max(max_album, key = lambda x:x[0])
            answer.append(max_song[1])
            max_album.remove(max_song)


        del best[max_key]


    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], 	[500, 600, 150, 800, 2500]))