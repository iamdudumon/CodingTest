def solution(id_pw, db):
    answer = ''
    
    dic = {user[0] : user[1] for user in db}

    if id_pw[0] in dic:
        answer = "login" if dic[id_pw[0]] == id_pw[1] else "wrong pw"
    else:
        answer = "fail"
    
    return answer