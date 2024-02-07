def solution(a, d, included):
    result = 0
    for i,check in enumerate(included):
        if check : # True면 합산
            result += a + d*i
    return result