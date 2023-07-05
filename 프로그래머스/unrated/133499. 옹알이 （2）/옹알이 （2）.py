def solution(babbling):
    answer = 0

    baby_speak = ["aya", "ye", "woo", "ma"]

    for bab in babbling:
        i = 0
        #print("-------", bab , "------")

        while i < len(baby_speak):
            bab_replace = bab.replace(baby_speak[i], str(i))     # replace에 마지막 인자를 안 주면 replaceAll 메소드와 같음!!
            #print(bab_replace)
            if str(i) + str(i) in bab_replace:                  # replace하는 문자를 str(i)로 해서 다른 변환 값과 중복되지 않게 구현
                break

            if bab != bab_replace:      #교체될 옹알이가 존재
                bab = bab_replace
          
            i = i + 1

        try:
            int(bab)            #try 문을 통해 bab가 오로지 숫자로만 구성돼있다면 예외처리가 일어나지 않고 옹알이가 교체 가능함을 의미!!
            answer = answer + 1
        except:
            pass

    return answer