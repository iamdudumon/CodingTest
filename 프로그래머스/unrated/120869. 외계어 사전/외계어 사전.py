def solution(spell, dic):
    spell_set = set(spell)
    
    for word in dic:
        temp = set(list(word))
        if spell_set.issubset(temp):
            return 1
            
    return 2