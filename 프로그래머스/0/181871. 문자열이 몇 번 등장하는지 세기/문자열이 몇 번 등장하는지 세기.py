def solution(myString, pat):
    answer = 0
    L = len(myString)
    l = len(pat)
    for i in range(L-l+1):
        if myString[i:i+l] == pat:
            answer += 1
    return answer