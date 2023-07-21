# def solution(phone_book):
#     answer = True

#     phone_book = sorted(phone_book)

#     for i in range(len(phone_book)):
#         if not answer:
#             break
#         for j in range(i + 1, len(phone_book)):
#             if phone_book[j][:len(phone_book[i])] == phone_book[i]:
#                 answer = False
#                 break

#     return answer

from functools import cmp_to_key

def compare(x, y):
    return len(x) - len(y)

def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book, key=cmp_to_key(compare))

    length = len(phone_book[0])
    i = 1
    
    while i < len(phone_book):
        start = i - 1

        while i < len(phone_book):
            if len(phone_book[i]) > length:
                break
            i += 1

        if i >= len(phone_book):
            break

        phone_dic = {}
        for j in range(i, len(phone_book)):
            phone = phone_book[j]
            phone_dic[phone[:length]] = phone

        for j in range(start, i):
            try:
                phone_dic[phone_book[j]]
                answer = False
                break
            except:
                pass

        if not answer:
            break

        length = len(phone_book[i])
    
    return answer

print(solution(["12","123","1235","567","88"]))