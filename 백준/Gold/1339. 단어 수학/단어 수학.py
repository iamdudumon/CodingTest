import sys

input = sys.stdin.readline

n = int(input())
alphabets = [input().rstrip() for _ in range(n)]
#al_set = set()
#for alphabet in alphabets:
#    for c in alphabet:
#        al_set.add(c)

alphabets.sort(reverse=True, key=lambda x : len(x))

alp_dic = {}
for alp in alphabets:
    alp_len = len(alp)
    for i, c in enumerate(alp):
        if c not in alp_dic:
            alp_dic[c] = 0
        alp_dic[c] += 10 ** (alp_len - i)

temp_list = list(alp_dic.items())
temp_list.sort(reverse=True, key=lambda x : x[1])
al_dic = {al[0] : 9 - i for i, al in enumerate(temp_list)}

sum = 0
for alphabet in alphabets:
    temp = 0
    for c in alphabet:
        temp = temp * 10 + al_dic[c]
    sum += temp

print(sum)