def solution(strArr):
    answer = []
    for s in strArr:
        if 'ad' in s:
            continue
        answer.append(s)
    return answer