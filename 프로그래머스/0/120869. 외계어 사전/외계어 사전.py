def solution(spell, dic):
    spell.sort()
    for d in dic:
        if sorted(d) == spell:
            return 1 
    return 2