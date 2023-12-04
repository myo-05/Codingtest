def solution(participant, completion):
    p = sorted(participant)
    c = sorted(completion)
    result = p[-1]
    for i in range(len(c)):
        if p[i] != c[i]:
            result = p[i]
            break
    return result